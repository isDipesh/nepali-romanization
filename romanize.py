import re

# https://nepalgo.tumblr.com/post/53364348267/vocabulary-western-loanwords
LOAN_WORDS = {
    # from English
    'रेडियो': 'radio',
    'कोट': 'coat',
    'डाक्टर': 'doctor',
    'स्कुल': 'school',
    'क्यान्सर': 'cancer',
    'ब्याग': 'bag',
    'टिकट': 'ticket',
    'सिनेमा': 'cinema',
    'फोटो': 'photo',
    'टेलिफोन': 'telephone',
    'फोन': 'phone',
    'क्यामेरा': 'camera',
    'कम्प्युटर': 'computer',
    'मोटर': 'motor',
    'मोबाइल': 'mobile',
    # from Latin
    'क्यालेन्डर': 'calendar',
    'क्याम्पस': 'campus',
    'स्टुडियो': 'studio',
    # from French
    'कलेज': 'college',
    'पुलिस': 'police',
    'इन्जिनियर': 'engineer',
    'टुरिस्ट': 'tourist',
    # from Portugese
    'कफी': 'coffee',
    'कर्फ्यु': 'curfew'
}

HARD_CODED = {
    'काठमाडौँ': 'Kathmandu',
    'गीत': 'geet',
    'तर': 'tara',
    'मञ्च': 'manch',
    'तँ': 'ta',
    'संयोजक': 'samyojak',
    ' प्रशंसा': 'prasamsha',
    'संलग्न': 'samlagna',
    'वर्ष': 'barsha',
    'नम्बर': 'number',
    'न.': 'No.',
    'नाम': 'naam',
    'छैन': 'chhaina',
    'दिन': 'din',
    'तल': 'tala',
    'बाट': 'bata'
}

PREDEFINED = LOAN_WORDS.copy()
PREDEFINED.update(HARD_CODED)

KARS = ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ', 'ं', 'ँ', '्', 'ृ', 'ः']
CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब',
              'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ']
VOWELS = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', ]
BINDUS = ['ँ', 'ं', 'ः', ]
# बिभाक्ति and other suffixes
SUFFIXES = ['ले', 'बाट', 'लाई', 'द्वारा', 'देखि', 'को', 'का', 'की', 'मा', 'हरु', 'संग', ' सँग', 'पनि', 'कै', ' स्थित']


def replace_char(char):
    rep_dct = {
        'क': 'ka', 'ख': 'kha', 'ग': 'ga', 'घ': 'gha', 'ङ': 'na',
        'च': 'cha', 'छ': 'chha', 'ज': 'ja', 'झ': 'jha', 'ञ': 'na',
        'ट': 'ta', 'ठ': 'tha', 'ड': 'da', 'ढ': 'dha', 'ण': 'na',
        'त': 'ta', 'थ': 'tha', 'द': 'da', 'ध': 'dha', 'न': 'na',
        'प': 'pa', 'फ': 'pha', 'ब': 'ba', 'भ': 'bha', 'म': 'ma',
        'य': 'ya', 'र': 'ra', 'ल': 'la', 'व': 'wa',
        'श': 'sha', 'ष': 'sha', 'स': 'sa', 'ह': 'ha',
        'ा': 'a', 'ि': 'i', 'ी': 'i', 'ु': 'u', 'ू': 'u', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au',
        'ं': 'an', 'ः': 'ah', 'ँ': 'an',
        'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'i', 'उ': 'u', 'ऊ': 'oo', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
        '्': '',
        'ृ': 'ri', 'ॠ': 'ri', 'ऋ': 'ri', 'ॐ': 'om',
        '१': '1', '२': '2', '३': '3', '४': '4', '५': '5', '६': '6', '७': '7', '८': '8', '९': '9', '०': '0'
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
    if word in PREDEFINED.keys():
        new = PREDEFINED[word]
    else:
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
    # Handle ज्ञ
    str = str.replace('ज्ञ', 'ग्य')
    romanized_str = re.sub(pattern, handle_matches, str)
    # Replace purna birams with full-stops
    romanized_str = romanized_str.replace(r' ।', '.').replace(r'।', '.')
    capitalized = capitalize(romanized_str)
    print(capitalized)
    return capitalized
