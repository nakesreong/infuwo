// State Management
let parablesData = null;
let currentLang = localStorage.getItem('infuwo-lang') || 'ru';
let theme = localStorage.getItem('infuwo-theme') || 'dark';

// DOM Elements
const parablesContainer = document.getElementById('parables-container');
const chapterList = document.getElementById('chapter-list');
const searchInput = document.getElementById('search-input');
const clearSearchBtn = document.getElementById('clear-search');
const themeToggle = document.getElementById('theme-toggle');
const langButtons = document.querySelectorAll('.view-selector .btn-toggle');
const footnotesPanel = document.getElementById('footnotes-panel');
const footnotesList = document.getElementById('footnotes-list');
const toast = document.getElementById('toast');

// Initialize App
async function init() {
    setupTheme();
    setupLanguageSelector();
    
    try {
        const response = await fetch('parables.json');
        if (!response.ok) throw new Error('Failed to load parables data');
        parablesData = await response.ok ? await response.json() : null;
        
        if (parablesData) {
            renderSidebar();
            renderContent();
            renderFootnotes();
            setupSearch();
            setupHashRouting();
            
            // If page loaded with a hash, handle it after rendering
            if (window.location.hash) {
                setTimeout(handleHashChange, 300);
            }
        }
    } catch (error) {
        console.error('Error initializing app:', error);
        parablesContainer.innerHTML = `<div class="loading">Ошибка загрузки мудрости. Пожалуйста, обновите страницу.</div>`;
    }
}

// Theme Configuration
function setupTheme() {
    document.body.className = `${theme}-theme`;
    themeToggle.addEventListener('click', () => {
        theme = theme === 'dark' ? 'light' : 'dark';
        document.body.className = `${theme}-theme`;
        localStorage.setItem('infuwo-theme', theme);
    });
}

// Language Selector Configuration
function setupLanguageSelector() {
    langButtons.forEach(btn => {
        // Set active state on load
        if (btn.dataset.lang === currentLang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }

        btn.addEventListener('click', (e) => {
            langButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentLang = btn.dataset.lang;
            localStorage.setItem('infuwo-lang', currentLang);
            
            // Adjust title lang
            updateSiteTitle();
            
            // Re-render contents
            renderContent();
        });
    });
    updateSiteTitle();
}

function updateSiteTitle() {
    const titleRu = document.getElementById('site-title-ru');
    const titleEn = document.getElementById('site-title-en');
    if (currentLang === 'en') {
        titleRu.classList.add('hidden');
        titleEn.classList.remove('hidden');
    } else {
        titleRu.classList.remove('hidden');
        titleEn.classList.add('hidden');
    }
}

// Render Sidebar Navigation
function renderSidebar() {
    chapterList.innerHTML = '';
    parablesData.chapters.forEach(chap => {
        const li = document.createElement('li');
        const title = currentLang === 'en' ? chap.chapter_title_en : chap.chapter_title_ru;
        li.innerHTML = `<a href="#chapter-${chap.chapter_id}" class="chapter-link" data-id="${chap.chapter_id}">Гл. ${chap.chapter_id}. ${title}</a>`;
        chapterList.appendChild(li);
        
        // Add click behavior to links
        li.querySelector('a').addEventListener('click', (e) => {
            e.preventDefault();
            const targetEl = document.getElementById(`chapter-${chap.chapter_id}`);
            if (targetEl) {
                targetEl.scrollIntoView({ behavior: 'smooth' });
                // Update active link styling
                document.querySelectorAll('.chapter-link').forEach(link => link.classList.remove('active'));
                e.target.classList.add('active');
            }
        });
    });
}

// Replace [fn:X] placeholder with footnote link
function parseFootnotes(text) {
    return text.replace(/\[fn:(\d+)\]/g, (match, fnId) => {
        return `<a href="#ftn${fnId}" class="fn-link" id="ref${fnId}">[${fnId}]</a>`;
    });
}

// Render Parables Content
function renderContent(query = '') {
    parablesContainer.innerHTML = '';
    const cleanQuery = query.toLowerCase().trim();
    let hasResults = false;

    parablesData.chapters.forEach(chap => {
        const chapTitle = currentLang === 'en' ? chap.chapter_title_en : chap.chapter_title_ru;
        
        // Filter parables
        const filteredParables = chap.parables.filter(p => {
            if (!cleanQuery) return true;
            const textRuCombined = p.text_ru.join(' ').toLowerCase();
            const textEnCombined = p.text_en.join(' ').toLowerCase();
            return p.id.includes(cleanQuery) || 
                   textRuCombined.includes(cleanQuery) || 
                   textEnCombined.includes(cleanQuery);
        });

        if (filteredParables.length > 0) {
            hasResults = true;
            const section = document.createElement('section');
            section.className = 'chapter-section';
            section.id = `chapter-${chap.chapter_id}`;
            
            section.innerHTML = `<h2>Глава ${chap.chapter_id}. ${chapTitle}</h2>`;
            
            const cardsContainer = document.createElement('div');
            cardsContainer.className = 'cards-container';
            
            filteredParables.forEach(parable => {
                const card = document.createElement('article');
                card.className = 'parable-card glass-panel';
                card.id = parable.id;
                
                // Share button text depending on lang
                const shareText = currentLang === 'en' ? 'Share' : 'Поделиться';
                
                let cardBodyHTML = '';
                
                if (currentLang === 'ru') {
                    cardBodyHTML = `
                        <div class="parable-body">
                            ${parable.text_ru.map(p => `<p class="parable-paragraph">${highlightText(parseFootnotes(p), cleanQuery)}</p>`).join('')}
                        </div>
                    `;
                } else if (currentLang === 'en') {
                    cardBodyHTML = `
                        <div class="parable-body">
                            ${parable.text_en.map(p => `<p class="parable-paragraph">${highlightText(parseFootnotes(p), cleanQuery)}</p>`).join('')}
                        </div>
                    `;
                } else { // Both languages (side-by-side)
                    cardBodyHTML = `
                        <div class="parable-body layout-both">
                            <div class="side-ru">
                                <span class="lang-label">🇷🇺 Русский</span>
                                ${parable.text_ru.map(p => `<p class="parable-paragraph">${highlightText(parseFootnotes(p), cleanQuery)}</p>`).join('')}
                            </div>
                            <div class="side-en">
                                <span class="lang-label">🇬🇧 English</span>
                                ${parable.text_en.map(p => `<p class="parable-paragraph">${highlightText(parseFootnotes(p), cleanQuery)}</p>`).join('')}
                            </div>
                        </div>
                    `;
                }

                card.innerHTML = `
                    <div class="parable-header">
                        <span class="parable-id">§ ${parable.id}</span>
                        <button class="btn-share" onclick="copyLink('${parable.id}')">
                            <span>🔗</span> ${shareText}
                        </button>
                    </div>
                    ${cardBodyHTML}
                `;
                
                cardsContainer.appendChild(card);
            });
            
            section.appendChild(cardsContainer);
            parablesContainer.appendChild(section);
        }
    });

    if (!hasResults) {
        parablesContainer.innerHTML = `<div class="loading">Суждений не найдено. Попробуйте другой запрос.</div>`;
    }
}

// Highlight matching search text
function highlightText(text, query) {
    if (!query) return text;
    // We only highlight matching words, avoiding wrapping inside HTML tags (like <a href...>)
    const regex = new RegExp(`(${escapeRegExp(query)})(?![^<]*>|[^<>]*</)`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// Render Footnotes
function renderFootnotes() {
    footnotesList.innerHTML = '';
    const notes = currentLang === 'en' ? parablesData.footnotes_en : parablesData.footnotes;
    
    Object.entries(notes).forEach(([id, text]) => {
        const li = document.createElement('li');
        li.id = `ftn${id}`;
        // Remove leading duplicate [id] from the footnote text
        const cleanText = text.replace(new RegExp(`^\\s*\\[${id}\\]\\s*`), '');
        li.innerHTML = `
            <strong>[${id}]</strong> ${cleanText}
            <a href="#ref${id}" class="back-link" title="Назад к тексту">↩</a>
        `;
        footnotesList.appendChild(li);
    });
}

// Copy Link Helper
window.copyLink = function(id) {
    const url = `${window.location.origin}${window.location.pathname}#${id}`;
    navigator.clipboard.writeText(url).then(() => {
        showToast();
    }).catch(err => {
        console.error('Could not copy link: ', err);
    });
};

function showToast() {
    toast.textContent = currentLang === 'en' ? 'Link copied to clipboard!' : 'Ссылка скопирована в буфер обмена!';
    toast.classList.remove('hidden');
    toast.style.opacity = 1;
    toast.style.transform = 'translateY(0)';
    
    setTimeout(() => {
        toast.style.opacity = 0;
        toast.style.transform = 'translateY(10px)';
        setTimeout(() => toast.classList.add('hidden'), 300);
    }, 2000);
}

// Search Functionality
function setupSearch() {
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value;
        if (query) {
            clearSearchBtn.classList.remove('hidden');
        } else {
            clearSearchBtn.classList.add('hidden');
        }
        renderContent(query);
    });
    
    clearSearchBtn.addEventListener('click', () => {
        searchInput.value = '';
        clearSearchBtn.classList.add('hidden');
        renderContent('');
    });
}

// Deep Linking & Hash Routing
function setupHashRouting() {
    window.addEventListener('hashchange', handleHashChange);
}

function handleHashChange() {
    const hash = window.location.hash;
    if (!hash) return;
    
    if (hash.startsWith('#chapter-')) {
        // Handled by smooth scroll event in renderSidebar
        return;
    }
    
    const targetId = hash.substring(1);
    const targetEl = document.getElementById(targetId);
    if (targetEl) {
        // Scroll target card into view
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        // Apply target CSS styling triggers
        targetEl.focus();
    }
}

// Run App on DOM load
window.addEventListener('DOMContentLoaded', init);
