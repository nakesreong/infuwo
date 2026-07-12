import sys
import re
import json
import html

def clean_html(text):
    # Remove HTML tags except superscript for footnotes (we will translate footnotes into custom tags or clean them)
    # Replace common spaces and clean whitespace
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&nbsp', ' ')
    text = text.replace('\r', '')
    
    # Replace footnote links with [fn:X]
    text = re.sub(r'<a\s+href=[^>]+><sup>(?:<font[^>]*>)?\s*\[(\d+)\]\s*(?:</font>)?</sup></a>', r' [fn:\1]', text)
    text = re.sub(r'<sup>(?:<font[^>]*>)?\s*\[(\d+)\]\s*(?:</font>)?</sup>', r' [fn:\1]', text)
    
    # Strip span tags, font tags, but keep text
    text = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', text)
    text = re.sub(r'<font[^>]*>(.*?)</font>', r'\1', text)
    
    # Remove other tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Decode HTML entities
    text = html.unescape(text)
    
    # Normalize double spaces and trim
    text = re.sub(r' +', ' ', text)
    text = text.strip()
    return text

def parse():
    sys.stdout.reconfigure(encoding='utf-8')
    with open('Инь Фу Во. Суждения о безопасности.html', 'r', encoding='windows-1251') as f:
        content = f.read()

    # Extract footnotes
    # Footnotes are in <div id="ftnX"> ... </div>
    footnote_matches = re.findall(r'<div\s+id="ftn(\d+)">\s*<p>(.*?)</p>\s*</div>', content, re.DOTALL)
    footnotes = {}
    for fn_num, fn_text in footnote_matches:
        footnotes[int(fn_num)] = clean_html(fn_text).replace('обратно', '').strip()
        
    print(f"Parsed {len(footnotes)} footnotes:")
    for num, txt in footnotes.items():
        print(f"  [{num}] {txt[:60]}...")

    # We also want to extract chapters and their parables.
    # Chapters start with <h2>Глава X. Название</h2>
    # Parables are marked by <h3>Y.Z</h3>
    # Let's split content into chapters first.
    # We can split by <h2>Глава
    chapter_splits = re.split(r'<h2>Глава(?:&nbsp;|\s)+(\d+)\.\s*(.*?)</h2>', content)
    
    # The first element is before Chapter 1.
    preamble = chapter_splits[0]
    
    chapters = []
    # chapter_splits will have [preamble, '1', 'О работниках', chapter_1_body, '2', 'О шифровании', chapter_2_body, ...]
    for idx in range(1, len(chapter_splits), 3):
        chap_num = int(chapter_splits[idx])
        chap_title = clean_html(chapter_splits[idx+1])
        chap_body = chapter_splits[idx+2]
        
        # Split body by <h3>Y.Z</h3>
        parable_splits = re.split(r'<h3>(\d+\.\d+)</h3>', chap_body)
        # The first element in parable_splits is introduction text or whitespace before the first parable.
        parables = []
        for p_idx in range(1, len(parable_splits), 2):
            p_id = parable_splits[p_idx]
            p_body = parable_splits[p_idx+1]
            
            # Extract paragraphs (<p>...</p>)
            p_paragraphs = re.findall(r'<p>(.*?)</p>', p_body, re.DOTALL)
            clean_paragraphs = [clean_html(p) for p in p_paragraphs if p.strip()]
            
            parables.append({
                "id": p_id,
                "text_ru": clean_paragraphs,
                "text_en": [] # To be filled in later
            })
            
        chapters.append({
            "chapter_id": chap_num,
            "chapter_title_ru": chap_title,
            "chapter_title_en": "", # To be filled in later
            "parables": parables
        })
        print(f"Chapter {chap_num}: '{chap_title}' - parsed {len(parables)} parables")

    data = {
        "footnotes": {str(k): v for k, v in footnotes.items()},
        "chapters": chapters
    }

    with open('parables_raw.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Parsed output successfully written to parables_raw.json")

if __name__ == '__main__':
    parse()
