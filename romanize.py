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
    rep_dct = {
        'क': 'ka',
        'ख': 'kha',
        'ग': 'ga',
        'घ': 'gha',
        'ङ': 'na',
        'च': 'cha',
        'छ': 'chha',
        'ज': 'ja',
        'झ': 'jha',
        'ञ': 'na',
        'ट': 'ta',
        'ठ': 'tha',
        'ड': 'da',
        'ढ': 'dha',
        'ण': 'na',
        'त': 'ta',
        'थ': 'tha',
        'द': 'da',
        'ध': 'dha',
        'न': 'na',
        'प': 'pa',
        'फ': 'pha',
        'ब': 'ba',
        'भ': 'bha',
        'म': 'ma',
        'य': 'ya',
        'र': 'ra',
        'ल': 'la',
        'व': 'wa',
        'श': 'sha',
        'ष': 'sha',
        'स': 'sa',
        'ह': 'ha',
        'ऋ': 'ri',
        'ा': 'a',
        'ि': 'i',
        'ी': 'i',
        'ु': 'u',
        'ू': 'u',
        'े': 'e',
        'ै': 'ai',
        'ॊ': 'o',
        'ो': 'o',
        'ौ': 'au',
        'अ': 'a',
        'आ': 'aa',
        'इ': 'i',
        'ई': 'i',
        'उ': 'u',
        'ऊ': 'oo',
        'ए': 'e',
        'ऐ': 'ai',
        'ओ': 'o',
        'औ': 'au',
        'ँ': 'an',
        'ं': 'an',
        'ः': 'ah',
        '्': '',
        'ृ': 'ri',
        'ॄ': 'r',
        'ॠ': 'ri',
        'ॣ': 'l',
        'ॢ': 'l',
        'ॐ': 'om'
    }
    return rep_dct[char] if char in rep_dct else char


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


def romanize_word(word):
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
        # Bindus after vowels and kars don't give 'a' sound
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
        new += romanize_word(suffix)
    return new


def handle_matches(match):
    word = match.group()
    if word in predefined_trans.keys():
        return predefined_trans[word]
    else:
        return romanize_word(match.group())


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


def capitalize(str):
    punctuation_indices = find_punctuations(str)
    lst = list(str)
    lst[0] = lst[0].upper()
    length = len(str)
    for idx in punctuation_indices:
        offset = 1
        if idx < length - 1:
            first_letter = lst[idx + offset]
            if first_letter == ' ' and idx < length - (offset + 1):
                offset = 2
                first_letter = lst[idx + offset]
            if first_letter in ['\n', '\t', '\r']:
                continue
            lst[idx + offset] = first_letter.upper()
    str = ''.join(lst)
    return str


def romanize_devanagari(str):
    pattern = r'[^\s,!\?\[\]\(\)।]+'
    romanized_str = re.sub(pattern, handle_matches, str)
    # Replace purna birams with full-stops
    romanized_str = romanized_str.replace(r' ।', '.').replace(r'।', '.')
    capitalized = capitalize(romanized_str)
    print(capitalized)
    return capitalized


romanize_devanagari('''मर्न बरु गाह्रो हुन्न-२, तिम्रो माया मार्नै सकिंन -२
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
