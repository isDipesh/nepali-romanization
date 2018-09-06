import re

predefined_trans = {
    'गीत': 'geet',
    'तर': 'tara',
    'मञ्च': 'manch',
    'तँ': 'ta',
    'संयोजक': 'samyojak',
    ' प्रशंसा': 'prasamsha',
    'संलग्न': 'samlagna',
    'वर्ष': 'barsha',
    'मोबाइल': 'mobile',
    'नम्बर': 'number',
    'न.': 'No.',
    'नाम': 'naam',
    'छैन': 'chhaina',
}

KARS = ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ', 'ं', '्', 'ृ', 'ः']
CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब',
              'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ']
VOWELS = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', ]
BINDUS = ['ँ', 'ं', 'ः', ]
# बिभाक्ति
SUFFIXES = ['ले', 'बाट', 'लाई', 'द्वारा', 'देखि', 'को', 'का', 'की', 'मा', 'हरु', 'संग', 'पनि']


def replace_char(char):
    char = char.replace(r'क', "ka")
    char = char.replace(r'ख', "kha")
    char = char.replace(r'ग', "ga")
    char = char.replace(r'घ', "gha")
    char = char.replace(r'ङ', "na")
    char = char.replace(r'च', "cha")
    char = char.replace(r'छ', "chha")
    char = char.replace(r'ज', "ja")
    char = char.replace(r'झ', "jha")
    char = char.replace(r'ञ', "na")
    char = char.replace(r'ट', "ta")
    char = char.replace(r'ठ', "tha")
    char = char.replace(r'ड', "da")
    char = char.replace(r'ढ', "dha")
    char = char.replace(r'ण', "na")
    char = char.replace(r'त', "ta")
    char = char.replace(r'थ', "tha")
    char = char.replace(r'द', "da")
    char = char.replace(r'ध', "dha")
    char = char.replace(r'न', "na")
    char = char.replace(r'प', "pa")
    char = char.replace(r'फ', "pha")
    char = char.replace(r'ब', "ba")
    char = char.replace(r'भ', "bha")
    char = char.replace(r'म', "ma")
    char = char.replace(r'य', "ya")
    char = char.replace(r'र', "ra")
    char = char.replace(r'ल', "la")
    char = char.replace(r'व', "wa")
    char = char.replace(r'श', "sha")
    char = char.replace(r'ष', "sha")
    char = char.replace(r'स', "sa")
    char = char.replace(r'ह', "ha")
    char = char.replace(r'ऋ', "ri")
    char = char.replace(r'ा', "a")
    char = char.replace(r'ि', "i")
    char = char.replace(r'ी', "i")
    char = char.replace(r'ु', "u")
    char = char.replace(r'ू', "u")
    char = char.replace(r'े', "e")
    char = char.replace(r'ै', "ai")
    char = char.replace(r'ॊ', "o")
    char = char.replace(r'ो', "o")
    char = char.replace(r'ौ', "au")
    char = char.replace(r'अ', "a")
    char = char.replace(r'आ', "aa")
    char = char.replace(r'इ', "i")
    char = char.replace(r'ई', "i")
    char = char.replace(r'उ', "u")
    char = char.replace(r'ऊ', "oo")
    char = char.replace(r'ए', "e")
    char = char.replace(r'ऐ', "ai")
    char = char.replace(r'ओ', "o")
    char = char.replace(r'औ', "au")
    char = char.replace(r'ँ', "an")
    char = char.replace(r'ं', "an")
    char = char.replace(r'ः', "ah")
    char = char.replace(r'्', "")
    char = char.replace(r'ृ', "ri")
    char = char.replace(r'ॄ', "r")
    char = char.replace(r'ॠ', "ri")
    char = char.replace(r'ॣ', "l")
    char = char.replace(r'ॢ', "l")
    char = char.replace(r'ॐ', "om")
    return char


def pronouce_inherent(word, char, idx):
    prev = word[idx - 1]
    # Scenarios when inherent vowel is pronounced
    # 1. छ, य, ह
    if char in ['छ', 'य', 'ह']:
        return True
    # 2. Followed by a dead consonant, or bindus
    if prev == '्' or prev in BINDUS:
        return True
    # 3. garera, parera, etc.
    if prev == 'े' and char == 'र' and len(word) > 3:
        return True
    # 4. bhanana, ganana, garana, jaana, laana, suna
    if char == 'न':
        return True
    # 5. Consonant after vowel, e.g. आज
    if prev in VOWELS:
        return True
    return False


def conv_word(word):
    # print(word)
    new = ''
    suffixes = []
    for suff in SUFFIXES:
        # if the word ends in suffix but isn't suffix itself
        if word.endswith(suff) and len(suff) != len(word):
            word = word[:len(suff) * -1]
            suffixes.insert(0, suff)
    length = len(word)
    for idx, char in enumerate(word):
        tr = replace_char(char)
        if char in BINDUS and idx > 0 and (word[idx - 1] in KARS or word[idx - 1] in VOWELS):
            if idx == length - 1:
                # Don't do anything for bindus at last like गरें => gare 
                tr = ''
            else:
                ## Don't write a
                tr = tr[1:]
        if char in CONSONANTS:
            # if the consonant is followed by kaars (a-kaars, u-kaars, etc.), remove trailing 'a'
            if idx < length - 1:
                if word[idx + 1] in KARS and tr[-1:] == 'a':
                    tr = tr[:-1]
            elif idx == length - 1 and char == 'ङ':
                tr = 'ng'
            # remove trailing 'a' from consonant if last character but only if it isn't the only character
            elif idx == length - 1 and len(word) > 1:
                if not pronouce_inherent(word, char, idx):
                    if tr[-1:] == 'a':
                        if char == 'व':
                            tr = 'va'
                        tr = tr[:-1]
        new += tr
    suffix = ''.join(suffixes)
    if suffix:
        new += conv_word(suffix)
    return new


def handle_matches(match):
    word = match.group()
    if word in predefined_trans.keys():
        return predefined_trans[word]
    else:
        return conv_word(match.group())


# https://www.daniweb.com/programming/software-development/threads/399829/sentence-capitalization-in-python#post1713277
def find_punctuations(str):
    positions = list()
    start = 0
    while start < len(str):
        pos = list()
        for c in ('.', '!', '?', '\n'):
            p = str.find(c, start)
            if p >= start:
                pos.append(p)
        if pos:
            m = min(pos)
            positions.append(m)
            start = m + 1
        else:
            break
    return positions


def conv(str):
    pattern = r'[^\s,!\?\[\]\(\)।]+'
    romanized_str = re.sub(pattern, handle_matches, str)
    romanized_str = romanized_str.replace(r' ।', ".")
    romanized_str = romanized_str.replace(r'।', ".")
    punctuation_indices = find_punctuations(romanized_str)
    # print(romanized_str)
    length = len(romanized_str)
    for idx in punctuation_indices:
        offset = 1
        if idx < length - 1:
            first_letter = romanized_str[idx + offset]
            if first_letter == ' ' and idx < length - (offset + 1):
                offset = 2
                first_letter = romanized_str[idx + offset]
            if first_letter in ['\n', '\t', '\r']:
                continue
            lst = list(romanized_str)
            lst[idx + offset] = first_letter.upper()
            romanized_str = ''.join(lst)
    print(romanized_str)


conv('''मर्न बरु गाह्रो हुन्न-२, तिम्रो माया मार्नै सकिंन -२
मर्न बरु गाह्रो हुन्न-२, तिम्रो माया मार्नै सकिंन -२

बसन्त को हरियाली फूल संगै ओइली जान्छ-२
निलो भुइँको सेतो बादल हावा संगै उडी जान्छ
तर तिम्रो न्यानो माया-२ अझैं पनि न्यानो नै छ
तिम्रो माया मार्नै सकिंन -२
मर्न बरु गाह्रो हुन्न-२, तिम्रो माया मार्नै सकिंन -२

धेरै लामो बाटो हामी संग संगै हिंडी सक्यौं-२
टाढा टाढा कता कता हामी दुवै पुगी सक्यौं
तर अन्त्य यसको यहीं-२ भन्न अझै मनै भएन
तिम्रो माया मार्नै सकिंन -२
मर्न बरु गाह्रो हुन्न-२, तिम्रो माया मार्नै सकिंन -२''')
