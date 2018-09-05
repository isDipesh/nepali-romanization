predefined_trans = {
    'गीत': 'geet'
}

KARS = ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ', 'ँ', 'ं', '्', 'ृ', 'ः']
CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब',
              'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ']
# बिभाक्ति
SUFFIXES = ['ले', 'बाट', 'लाई', 'द्वारा', 'देखि', 'को', 'का', 'की', 'मा', 'हरु', 'संग','पनि']

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
    char = char.replace(r'ञ', "ny")
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
    char = char.replace(r'ॆ', "e")
    char = char.replace(r'े', "e")
    char = char.replace(r'ै', "ai")
    char = char.replace(r'ॊ', "o")
    char = char.replace(r'ो', "o")
    char = char.replace(r'ौ', "au")
    char = char.replace(r'अ', "a")
    char = char.replace(r'आ', "aa")
    char = char.replace(r'इ', "i")
    char = char.replace(r'ई', "ee")
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
    char = char.replace(r'।', ".")
    char = char.replace(r' ।', ".")
    char = char.replace(r'ृ', "ri")
    char = char.replace(r'ॄ', "r")
    char = char.replace(r'ॠ', "ri")
    char = char.replace(r'ॣ', "l")
    char = char.replace(r'ॢ', "l")
    char = char.replace(r'ॐ', "om")
    return char


def conv_word(word):
    # print(word)
    new = ''
    for suffix in SUFFIXES:
        if word.endswith(suffix):
            word = word.rstrip(suffix)
            print(suffix)
            print(word)
    length = len(word)
    for idx, char in enumerate(word):
        tr = replace_char(char)
        if char in CONSONANTS:
            # if the consonant is followed by kaars (a-kaars, u-kaars, etc.), remove trailing 'a'
            if idx < length - 1:
                if word[idx + 1] in KARS and tr[-1:] == 'a':
                    tr = tr[:-1]
            # remove trailing 'a' from consonant if last character but only if not previous character is half
            elif idx == length - 1 and not word[idx - 1] == '्':
                if tr[-1:] == 'a':
                    tr = tr[:-1]
        new += tr
    return new


def conv(str):
    new_words = []
    for word in str.split(' '):
        if word in predefined_trans.keys():
            new_word = predefined_trans[word]
        else:
            new_word = conv_word(word)
        new_words.append(new_word)
    new_str = ' '.join(new_words)
    print(new_str)


# conv('जीवन हुरीको गीत हो भने जसरि पनि गाउनै पर्छ सुखी मिलेन भने हामी दुखि दुखि नै मिल्नुपर्छ')
# conv('मेरा घरहरु गिर्छन्')
print(conv_word('घरहरु'))
