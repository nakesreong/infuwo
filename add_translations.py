import json

# Dictionary of translations for all parables
translations = {
    # Chapter titles
    "chapters": {
        1: "About Employees",
        2: "About Encryption",
        3: "About Ethics",
        4: "About Information"
    },
    
    # Footnotes
    "footnotes": {
        "1": "Yin Fu Wo (廕傁幄) – the venerable protector Yin.",
        "2": "Yin Fu Wo refers to a program that performs encryption and decryption based on an algorithm.",
        "3": "Yin Fu Wo calls the operating system and the hardware platform (the computer itself) the 'environment'.",
        "4": "From 'blackhole', which means routing the corresponding traffic to /dev/null.",
        "5": "QoS, Quality of Service – a traffic prioritization system.",
        "6": "DRM – Digital Rights Management, technical means of protecting copyright.",
        "7": "Access Control List — a list of permissions associated with an object.",
        "8": "Obviously, Yin Fu Wo refers to the name in conjunction with the Social Security Number."
    },
    
    # Parable translations
    "parables": {
        "1.1": [
            "Once, the Sysadmin complained to the Master:",
            "– We issued individual passwords to all our users, but they refuse to keep them secret. They write them on pieces of paper and stick them to their monitors. What should we do? How can we force them?",
            "Yin Fu Wo asked:",
            "– First tell me, why do they do this?",
            "The Sysadmin thought and replied:",
            "– Perhaps they do not think the password is valuable?",
            "– And is the password itself valuable?",
            "– Not by itself. The information protected by the password is valuable.",
            "– For whom is it valuable?",
            "– For our enterprise.",
            "– And for the users?",
            "– For the users, apparently not.",
            "– Exactly, – said the Master. – There is nothing of value to our employees under the password. We must make sure there is.",
            "– What is valuable to them? – asked the Sysadmin.",
            "– Guess in three tries, – the Master laughed.",
            "The Sysadmin left enlightened and created personal pages for all employees on the corporate portal. On those pages, the size of their salary was displayed. Upon learning this, all users began to worry about their passwords. The next day, the main topic of conversation in the smoking room was the Chief Accountant's salary. On the third day, not a single sticky note with a password was to be seen."
        ],
        "1.2": [
            "Once, the Sysadmin complained to the Master:",
            "– Our Tech Director refuses to follow security requirements. Everyone is supposed to have an antivirus, but he won't install it. How can we influence him?",
            "– Try to convince him, – said Yin Fu Wo.",
            "The Sysadmin went to convince him, but soon returned disappointed:",
            "– I could not convince him, Master.",
            "– Why did that happen? – asked Yin Fu Wo, and immediately added: – But answer honestly, without bias or resentment.",
            "The Sysadmin thought, lowered his eyes, and said softly:",
            "– Probably because he knows more about information security than I do.",
            "– Well, if the Tech Director knows more than you do, which is not surprising at all, – noted the Master, – then he knows best where an antivirus is needed and where it is not.",
            "– But what about the Security Policy! – exclaimed the Sysadmin.",
            "– And who wrote this Policy?",
            "The Sysadmin looked down and said:",
            "– I did.",
            "The Master remained wisely silent, and the Sysadmin left enlightened."
        ],
        "1.3": [
            "Once, in the smoking room, users began to complain that the Sysadmin had blocked everyone's access to the 'Odnoklassniki' social network. Yin Fu Wo heard about this and frowned.",
            "– Why did you block access for the people? – he asked the Sysadmin as they drank coffee after a smoke break.",
            "– Because such websites are not needed for work.",
            "– And is smoking needed for work?",
            "– Well, not really...",
            "– And drinking coffee?",
            "– Well...",
            "– Well then, – said the Master, – unblock access for the people."
        ],
        "1.4": [
            "Once, the Sysadmin wanted to install a security scanner in the local network.",
            "Yin Fu Wo said:",
            "– Do not do this.",
            "– But why?",
            "– There are a hundred computers in our network. The scanner will find two or three vulnerabilities on each of them.",
            "– Well, yes, it will...",
            "– And what will you do with these vulnerabilities?",
            "The Sysadmin fell into thought and answered nothing to the Master. He did not install the security scanner."
        ],
        "1.5": [
            "Once, the Sysadmin complained to the Master:",
            "– Antivirus doesn't help. It's installed on all workstations and updates twice a day. Yet every week someone gets infected and loses data.",
            "Yin Fu Wo shook his head with regret.",
            "– We must do something, – continued the Sysadmin.",
            "The Master nodded slightly. The Sysadmin asked:",
            "– What is better: to install a new multi-engine antivirus for everyone or to set up a centralized backup system?",
            "Yin Fu Wo replied:",
            "– Conduct training courses for the users."
        ],
        "1.6": [
            "Once, the Director decided to hire a junior technician (an enikeyist). Yin Fu Wo found a candidate, talked to him, and was satisfied. He said to the Director:",
            "– This man has turned his thoughts toward learning. Perhaps he will make a worthy employee.",
            "But the Chief of Security began to object:",
            "– This man has a criminal record. He cannot be hired.",
            "Then Yin Fu Wo asked:",
            "– How did you find out about this?",
            "– I have connections.",
            "The venerable Yin's face darkened, and he said to the Director:",
            "– Which of the two employees is more virtuous? The first committed a crime and paid his due punishment, which might have taught him a lesson. The second committed a crime himself by bribing a public official, yet feels no guilt and will never be punished. Which of these two is worthy of promotion?",
            "The Chief of Security silently stood up and walked out."
        ],
        "1.7": [
            "Once, the Director asked Yin Fu Wo about protection from internal threats. The Master said:",
            "– In the outside world, there are a hundred people who would like to obtain confidential information from your network. And there are five who are capable of doing so. But those hundred are unlikely to meet those five.",
            "The Master also said:",
            "– But in your internal network, there are five users who would like to obtain confidential information. And there are a hundred who can do so. And they have already met."
        ],
        "1.8": [
            "Once, the Director came to the protector Yin for advice. The Director said:",
            "– I would like to force all users to follow strict security rules. But then they will be offended by me and will work worse. I would like to give users complete freedom. But then they will catch viruses, disclose confidential information, and our business will suffer. How do I find the middle ground?",
            "Yin Fu Wo replied:",
            "– The height of a fence is equal to the height of its lowest section. The strength of a chain is equal to the strength of its weakest link. Force the most negligent of the users to follow those security rules that all the others follow without compulsion.",
            "– How simple! – exclaimed the Director and left enlightened."
        ],
        "1.9": [
            "The Director asked the venerable Yin:",
            "– I am offered to buy an unauthorized access protection system. Is it worth the money they are asking for it?",
            "Yin Fu Wo asked in return:",
            "– How many cases of unauthorized access have you had in the last three years?",
            "– None, – replied the Director.",
            "– And how many laptops and flash drives did your employees lose during this time?",
            "– Two laptops, – replied the Director, – and nobody counted the flash drives.",
            "– Why not buy a system for encrypting information on laptops and flash drives instead? – said Yin Fu Wo."
        ],
        "1.10": [
            "Once, the Director asked the venerable protector Yin about protection from internal threats. He said:",
            "– The internal enemy is either malicious or careless. The careless enemy is like raindrops, which are numerous and fly at the whim of the wind. It is easy to shield yourself from the rain with an umbrella. The malicious enemy is like a mosquito that bites in an unprotected spot. You cannot shield yourself from it with an umbrella.",
            "The Director asked further:",
            "– And which insider is worse, the malicious or the careless one?",
            "Yin Fu Wo replied:",
            "– One cannot frame the question this way. Both are worse."
        ],
        "1.11": [
            "Once, the Sysadmin asked:",
            "– Master, would you like a beautiful picture for your desktop? I have a collection of wallpapers with the starry sky and the moral law.",
            "– Why do you think my current wallpaper is worse? – asked Yin Fu Wo in return.",
            "– I don't know what picture you have now. I have never seen your desktop. You always have many windows open.",
            "– I have never seen it either, – said the venerable Yin. – I work."
        ],
        "1.12": [
            "Once, the junior accountant Li Chang brought a cactus as a gift to Yin Fu Wo.",
            "– Put it near your monitor, Master, – she said. – This cactus will protect you from harmful radiation.",
            "– Take it to the Sysadmin, – said Yin Fu Wo. – The cactus won't help me.",
            "– Why? – Li Chang asked, offended.",
            "– There is no driver for it under FreeBSD, – replied the Master."
        ],
        "1.13": [
            "Once, a seller of cheap and low-quality goods from the Xianggang province wandered into the office. He walked around the room and tried to sell something to everyone.",
            "Yin Fu Wo said to the Sysadmin:",
            "– You always say and write in your blog that spammers should be killed. Look, this is a spammer.",
            "– That's not the same kind of spammer, – muttered the Sysadmin.",
            "– You won't even call security? – the Master asked mockingly.",
            "The Sysadmin answered nothing. He was intensely hammering away at his keyboard."
        ],
        "1.14": [
            "The Sysadmin asked the Master:",
            "– The article says that any increase in security reduces employee loyalty. Is this true?",
            "Yin Fu Wo replied:",
            "– In reality, increasing security reduces convenience. Reducing convenience increases fatigue. Increasing fatigue reduces conscientiousness. And reducing the conscientiousness of employees is precisely what should be avoided.",
            "– Then what is loyalty? – asked the Sysadmin.",
            "– 'Loyalty', – Yin Fu Wo chuckled, – is something the Japanese invented so they wouldn't have to pay money."
        ],
        "1.15": [
            "Once, the Sysadmin complained to the Master:",
            "– Our Director understands absolutely nothing about IT. I cannot explain things to him. And his instructions are always so ridiculous.",
            "Yin Fu Wo replied:",
            "– This is the normal order of things. His concern is people and money. Your concern is hardware and software. You speak different languages.",
            "The Sysadmin agreed and asked:",
            "– How can we learn each other's language?",
            "– It is almost impossible, – said the Master. – For that, the Director would have to work as a sysadmin for several years, but he won't wish to. For that, you would have to work as a manager for several years, but they won't let you.",
            "– How then can those who speak different languages understand each other? – asked the Sysadmin.",
            "Yin Fu Wo replied:",
            "– Especially for these purposes, an intermediate language accessible to both has been created. Its name is 'GOST-17799'.",
            "– How simple! – exclaimed the Sysadmin and left enlightened."
        ],
        
        # Chapter 2
        "2.1": [
            "Once, the Sysadmin asked the venerable protector Yin:",
            "– Master, why don't you use digital signatures?",
            "– Reliable digital signatures have no certificate. Certified ones have no convenience. Convenient ones have no reliability, – replied Yin Fu Wo."
        ],
        "2.2": [
            "Yin Fu Wo spent two days setting up a VPN tunnel for his personal computer. When the tunnel was working, Yin sat down, respectfully facing south, and began to read his friendfeed.",
            "– Oh, Master, – the Sysadmin asked him, – I cannot understand, why do you need a VPN?",
            "– Do you not know that in a VPN tunnel all traffic is encrypted? – Yin wondered.",
            "– I know. But your tunnel terminates on an ordinary server in the country of western barbarians. And after that, all your jade traffic goes through the Net in the clear.",
            "– The network does not care about my traffic, which cannot be said about the ISP, – replied the Master. Seeing that the Sysadmin did not understand, he added: – For example, you trusted the bank with your money.",
            "The Sysadmin nodded.",
            "– But you cannot trust your own wife with all your money, – continued the wise Yin. – Why? Because she might consider this money to be hers. But that won't happen with the bank.",
            "The enlightened Sysadmin left to set up a VPN tunnel for himself."
        ],
        "2.3": [
            "The Sysadmin asked Yin Fu Wo:",
            "– Is it true that any cipher can be broken?",
            "The Master replied:",
            "– It can. But not the 'cipher', but a system of four: the algorithm, the implementation [fn:2], the environment [fn:3], and the operator.",
            "The Sysadmin asked further:",
            "– And which of these four is the most fragile?",
            "– The joints between them, – replied the Master."
        ],
        "2.4": [
            "Once, the Investigator turned to the venerable protector Yin. He asked:",
            "– Master, can you decrypt a PGPdisk cryptocontainer without knowing the password?",
            "– I cannot, – replied Yin Fu Wo. – And nobody else can.",
            "– Then woe to me! – exclaimed the Investigator. – Then I have no proof.",
            "– Seeing a locked lock, an ordinary man wishes to look inside. But a noble man knows that the most valuable things do not lie under lock, – said the Master. – What exactly do you wish to prove?",
            "– Violation of software copyrights.",
            "– Leave the cryptocontainer alone, – replied the Master. – Witness testimonies will be more than enough."
        ],
        "2.5": [
            "Yin Fu Wo said:",
            "– Encryption is the exchange of a large secret for a small secret. This small one must fit in the head. When a password is kept worse in the head than in the computer, encryption brings no benefit."
        ],
        "2.6": [
            "Once, the Sysadmin and the engineer Cha Win respectfully approached the Master, and the Sysadmin said:",
            "– My colleague Win claims that in all publicly released cryptographic programs there is a 'backdoor' made by special services. But I believe that this is not so. Which of us is right?",
            "Yin Fu Wo replied:",
            "– With this question, all engineers and all sysadmins begin their journey. He who has settled the answer to it for himself has stopped forever and cannot follow the Dao. However, neglecting this question is also incorrect.",
            "Then the venerable Yin continued:",
            "– The northern barbarians have such a legend. The fierce and wise Tiger, the king of beasts, ordered the Fox to build a duck farm. The foolish Fox made a secret path for himself during construction to steal state ducks. And, of course, he was caught immediately. The Tiger ordered the execution of the cheater and thus saved money on construction. Do not think, precious Win, that special services are like the foolish Fox. But you are by no means the wise Tiger, the king of beasts.",
            "The disciples left enlightened. After this, the Sysadmin refused encryption of his disk altogether. And the engineer Cha Win made a cryptocontainer inside a cryptocontainer."
        ],
        "2.7": [
            "The Sysadmin wished to select a strong password for centralized authorization via a RADIUS server. He turned to Yin Fu Wo for advice.",
            "– What do you think, Master, is the password '史達林格勒戰役' strong?",
            "– No, – replied Master Yin, – that is a dictionary password.",
            "– But such a word is not in dictionaries...",
            "– 'Dictionary' means that this combination of characters is in wordlists, which are connected to cryptanalysis programs. These dictionaries are compiled from all combinations of characters that have ever been seen on the Net.",
            "– And would the password 'Pft,bcm' work?",
            "– Unlikely. It is also a dictionary password."
        ],
        "2.8": [
            "Once, the engineer Cha Win turned to the Master:",
            "– A respectable man told me that encrypting email is wrong. Since an honest man has nothing to hide, encrypted correspondence will inevitably attract the attention of the Guarding Department. Master, what do you think about this?",
            "Yin Fu Wo replied:",
            "– A noble man has a sense of modesty. He covers his nakedness with clothes. Not at all because others beholding it will bring him harm. But such is the will of Heaven, and such is the ritual. An honest man has things to hide."
        ],
        "2.9": [
            "The engineer Cha Win sat over a project for a long time, and then complained to the Master:",
            "– I cannot reconcile backup and encryption. One keeps interfering with the other all the time.",
            "Yin Fu Wo replied:",
            "– They are irreconcilable. Encryption protects confidentiality. Backup protects availability. Confidentiality and availability are different protections.",
            "– But what should be done then? – asked Cha Win. – We need both confidentiality and availability here.",
            "– Let one be inside the other. Let the first not know about the second.",
            "The engineer Cha Win asked the Master:",
            "– What does backup inside encryption mean?",
            "– Let all file systems be encrypted, and let files be backed up from one to another, – replied Yin Fu Wo.",
            "Cha Win also asked:",
            "– What does encryption inside backup mean?",
            "– Make a backup copy of the cryptocontainer as a file, – replied Yin Fu Wo."
        ],
        "2.10": [
            "The Director said:",
            "– Why should we encrypt the contents of our disks? Why do we need a VPN? We have no illegal information.",
            "The wise Yin Fu Wo replied:",
            "– Sinlessness is not the result of righteousness, but the result of naivety."
        ],
        
        # Chapter 3
        "3.1": [
            "The Sysadmin asked:",
            "– Master, is it permissible to blackhole traffic in the event of a DoS attack?",
            "– Sometimes it is, – replied Yin Fu Wo.",
            "– And in which cases?",
            "– In which cases can a doctor cause harm to his patient? – the Master asked in return.",
            "– Probably when the prevented harm exceeds the harm caused, – the Sysadmin replied, after some thought.",
            "– Now I will ask something else, – continued the Master. – In which cases can a doctor cause harm to a bystander?",
            "– I do not know of such cases, – replied the Sysadmin.",
            "– Now you are ready to blackhole [fn:4] the necessary traffic, – the Master nodded.",
            "And the Sysadmin left enlightened."
        ],
        "3.2": [
            "Yin Fu Wo, walking through the office, looked at the employees' monitors. Having made his way to his workstation, he uttered:",
            "– Our engineer Cha Win is now configuring QoS [fn:5]. He thinks he is interacting with technology, but in reality, he is interacting with people. Our accountant Li Chang is now chatting on ICQ. She thinks she is communicating with a person, but in reality, she is communicating with a program.",
            "– Master, why is your monitor turned with its screen to the wall? – Li Chang asked.",
            "– To see people all the time, – replied the Master."
        ],
        "3.3": [
            "The engineer Cha Win wanted to work in the information security department. Yin Fu Wo told him:",
            "– You are not ready yet. You imagine yourself as a network warrior. But we need a network doctor."
        ],
        "3.4": [
            "Once, the engineer Cha Win reported:",
            "– I found a vulnerability in the 'Lin' program. What do you think about this, Master?",
            "– We must inform the Vendor.",
            "After some time, Cha Win came to the venerable protector Yin again.",
            "– I wrote to the Vendor about the vulnerability. They replied that they would close the vulnerability only in the next version. It will be released in six months.",
            "Yin Fu Wo's face darkened:",
            "– Write to them that we will publish this vulnerability in exactly two weeks.",
            "Three days later, a patch for the 'Lin' program was released.",
            "– And if they hadn't released the patch? – the Sysadmin asked the Master. – Would you have allowed Cha Win to publish the vulnerability?",
            "Yin Fu Wo smiled gently and said:",
            "– No. The Dao of information security is beautiful precisely because you cannot walk it alone. As soon as you outpace others, others quicken their pace. As soon as you break away from others, you have left the Dao."
        ],
        "3.5": [
            "After reading an article in a magazine, the Master noted:",
            "– Man is not the 'weakest link in information security'. Man is not a link at all."
        ],
        "3.6": [
            "Once, the Sysadmin asked:",
            "– Master, you always say that we must share knowledge in the field of information protection with everyone who wishes to learn.",
            "Yin Fu Wo nodded. The Sysadmin continued:",
            "– But there is also dangerous knowledge! Especially knowledge in information security.",
            "Yin Fu Wo exclaimed:",
            "– Dangerous knowledge?! Knowledge is dangerous for him who does NOT possess it."
        ],
        "3.7": [
            "Once, the Tech Director emailed a question to the venerable Yin. The Master replied by putting a fragment of a config file in the email. Except for the config and the signature, there was nothing in the reply.",
            "The Sysadmin, who received copies of both emails, asked:",
            "– Master, why did you put only a few commands in the email but did not add a single word?",
            "Yin Fu Wo quoted his own teacher in reply:",
            "– 'I do not wish to speak. Does Heaven speak? Yet the four seasons run their course.'"
        ],
        "3.8": [
            "The engineer Cha Win asked:",
            "– Should we strive for retribution when protecting information? Or should we use only passive defense?",
            "– It depends on who the opponent is, – replied the Master. – If a mosquito bites you, it should be slapped. If rain falls on you, you should cover yourself with an umbrella.",
            "– I understand. In many cases, a security incident is a force of nature. And nobody is to blame for it.",
            "Yin Fu Wo shook his head:",
            "– Not quite. Indeed, nobody is to blame for the fact that it started raining. But if an earthquake happened and a building collapsed that was supposed to stand, then there is someone to blame. And he will be punished.",
            "Cha Win left in thought."
        ],
        "3.9": [
            "The Master said:",
            "– Knowledge in information security is like a weapon. Would a warrior refuse to share his weapon with another who wants to protect his land? And we are, after all, in a state of war."
        ],
        "3.10": [
            "Once, Yin Fu Wo blocked several IP addresses on the firewall. The Sysadmin asked him for the reasons. The Master said:",
            "– Just in case. I saw unexplained behavior of the programs.",
            "– Maybe it's just a glitch? – the Sysadmin suggested.",
            "Yin Fu Wo replied:",
            "– Each of us sometimes faces the unexplained. Without understanding the essence, everyone acts in their own way. The Sysadmin performs rituals with a tambourine. The engineer Cha Win drinks beer and reinstalls the system. And I start to suspect the actions of a cunning enemy.",
            "The engineer Cha Win, hearing the conversation, noted:",
            "– That sounds like paranoia.",
            "– Paranoia is part of my job description, – replied the Master."
        ],
        "3.11": [
            "Once, a Hacker came to the venerable protector Yin.",
            "– Oh, wise Yin, – he said, – teach me your art.",
            "– Before that, you will have to pass a test. Hack this computer, – and Yin Fu Wo wrote an IP address on a piece of paper.",
            "– But that is my own computer! – the Hacker was surprised.",
            "– Precisely, – the Master confirmed. – You must hack it without using the passwords you know.",
            "The Hacker completed the test in one hour.",
            "– I will teach you, – said Yin Fu Wo.",
            "Three years later, the Master gave the Hacker the same task. The Hacker could not complete it.",
            "– Now your training is finished, – said Yin Fu Wo."
        ],
        "3.12": [
            "Yin Fu Wo said:",
            "– An information protector does not eliminate threats. He redistributes threats among people. From the less trusted to the more trusted."
        ],
        "3.13": [
            "The junior accountant Li Chang asked:",
            "– Master, why does everyone call our engineer Cha Win (奓蟁)? After all, according to his passport, he is Cha Sun (奓诵).",
            "Yin Fu Wo replied:",
            "– Look at him, how is he a Sun? When he loses client data, he disables the port on the switch and waits for the client to call. What kind of Sun is he?"
        ],
        
        # Chapter 4
        "4.1": [
            "When the army set out on a campaign to reason with the southern barbarians, a state official turned to Yin Fu Wo. He said:",
            "– Precious colleague Yin, help us wage information warfare on the Internet.",
            "Yin Fu Wo replied:",
            "– The Internet is words. If it has come to reasoning by force of arms, reasoning with words has ended."
        ],
        "4.2": [
            "The engineer Cha Win asked the Master about the abuse service. Yin Fu Wo said:",
            "– We need to write a regulation on receiving and processing complaints.",
            "– Why? – asked Cha Win. – Is it not enough just to follow the Dao?",
            "– Courage without ritual leads to rebellion. Truthfulness without ritual leads to rudeness. Loyalty without ritual leads to sycophancy, – replied the Master. – And information security without ritual leads to a loss of connectivity."
        ],
        "4.3": [
            "Once, the Director called a meeting on combating information leaks. When other employees had reported, Yin Fu Wo said:",
            "– The Chief of Security wrote ten thousand lines of orders and instructions. In doing so, he thought of people as machines. Therefore, his instructions will not be followed. The Sysadmin wrote seventy-seven rules for the DLP system. In doing so, he thought of machines and forgot about people. Therefore, his rules will harm the business.",
            "– In that case, – said the Director, – let them work together. Let them create a set of organizational and technical measures that will be followed and will facilitate business.",
            "Yin Fu Wo shook his head:",
            "– Two one-armed men cannot shoot a bow."
        ],
        "4.4": [
            "Cha Win asked:",
            "– Can a computer with Windows be secure?",
            "– In principle, it can, – replied Yin Fu Wo.",
            "– And in practice?",
            "The venerable protector Yin looked at the laptop Cha Win was holding in his hand, then said:",
            "– Sometimes an armored limousine is made for a president. But for a warrior, a tank is better."
        ],
        "4.5": [
            "The Sysadmin asked Yin Fu Wo about intellectual property. The Master said:",
            "– Great works belong to Heaven. Good works belong to people. Bad works belong to corporations.",
            "The Sysadmin also asked about DRM [fn:6] and copy protection. Yin Fu Wo replied:",
            "– Protecting a work consists precisely in copying it. Prohibiting copying is prohibiting protection."
        ],
        "4.6": [
            "Once, the conversation turned to parental control. The disciples asked Yin Fu Wo:",
            "– Is it necessary to restrict children's access to content containing violence?",
            "The Master replied:",
            "– Upbringing without violence will yield a generation incapable of violence. And a people incapable of violence will not survive surrounded by barbarian tribes.",
            "The disciples also asked:",
            "– Is it necessary to restrict children's access to content containing erotica?",
            "– It is impossible to restrict access to what you always carry with you.",
            "The disciples also asked:",
            "– Is it necessary to restrict children's access to content promoting drugs?",
            "– Prohibiting the promotion of the forbidden is as unwise as promoting the prohibition of promotion. One public execution of a drug dealer brings more benefit than ten thousand ACLs [fn:7]."
        ],
        "4.7": [
            "The Sysadmin asked the Master:",
            "– Why do the western barbarians protect personal data? What an unwise waste of resources!",
            "– In ancient times, the barbarians believed that knowing a person's true name [fn:8] allows one to cast a curse on them, – replied Yin Fu Wo.",
            "The Sysadmin was surprised:",
            "– But they have not been wild for a long time and know that witchcraft does not exist.",
            "– Yes, they know it now, – confirmed Master Yin. – But while they lived in wildness and hid their names, they managed to build a system that relies on the confidentiality of personal data. Now they have no other way.",
            "– It is good that we are civilized people and do not believe in witchcraft, – noted the Sysadmin.",
            "Yin Fu Wo smiled sadly:",
            "– Fearing witchcraft, the barbarians made witchcraft a reality. Knowing a person's true name [fn:8] allows one to steal their money."
        ],
        "4.8": [
            "Cha Win asked the Master:",
            "– Is it permissible to read someone else's email to prevent leaks?",
            "– You know yourself that it is not, – was the answer.",
            "– But the communication channels belong to the enterprise. This means all messages in them belong to it too.",
            "Yin Fu Wo shook his head:",
            "– Every day at lunch you receive a large bowl of rice from the enterprise. To whom, then, does your life belong?"
        ],
        "4.9": [
            "Once, at lunch, the Sysadmin asked Yin Fu Wo:",
            "– Master, why do you spend half an hour every morning studying logs? Wouldn't it be better to install an automated analyzer?",
            "Master Yin pointed to the chopsticks and said:",
            "– You may have heard that the northern barbarians do not know chopsticks. They eat their food with spoons. And they use automated log analyzers. Therefore, their lifespan is short, and their servers are easy to hack.",
            "Yin Fu Wo also said:",
            "– And the western barbarians eat with their hands. And they do not study logs at all. Therefore, they are all monstrously fat, and their servers are a public thoroughfare. We, unlike the barbarians, eat with chopsticks.",
            "The Sysadmin slowly finished his rice with shrimp and left enlightened to read logs."
        ],
        "4.10": [
            "The disciples asked Yin Fu Wo about the future of the Internet. The Master said:",
            "– The times of sellers of knowledge have passed. The times of sellers of anonymity have arrived. To find out is cheap, to hide is expensive."
        ]
    }
}

def merge():
    with open('parables_raw.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Set translated titles and parable translations
    for chapter in data['chapters']:
        ch_id = chapter['chapter_id']
        chapter['chapter_title_en'] = translations['chapters'][ch_id]
        
        for parable in chapter['parables']:
            p_id = parable['id']
            if p_id in translations['parables']:
                parable['text_en'] = translations['parables'][p_id]
            else:
                print(f"Warning: Missing translation for parable {p_id}")
                parable['text_en'] = []

    # Save translated footnotes
    data['footnotes_en'] = translations['footnotes']
    
    with open('parables.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Merged and wrote translated data to parables.json successfully!")

if __name__ == '__main__':
    merge()
