predefined_trans = {
    'गीत': 'geet',
    'तर': 'tara'
}

KARS = ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ', 'ँ', 'ं', '्', 'ृ', 'ः']
CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब',
              'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ']
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
    suffixes = []
    for suff in SUFFIXES:
        # if the word ends in suffix but isn't suffix itself
        if word.endswith(suff) and len(suff) != len(word):
            word = word[:len(suff) * -1]
            suffixes.insert(0, suff)
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
    suffix = ''.join(suffixes)
    if suffix:
        new += conv_word(suffix)
    return new


def conv(str):
    str = str.replace('\n', ' \n')
    new_words = []
    for word in str.split(' '):
        # handle new line for predefined words
        first_word = word.startswith('\n')
        last_word = word.endswith('\n')
        word = word.strip('\n')
        if word in predefined_trans.keys():
            new_word = predefined_trans[word]
            if first_word:
                new_word = '\n' + new_word
            if last_word:
                new_word += '\n'
        else:
            new_word = conv_word(word)
        new_words.append(new_word)
    new_str = ' '.join(new_words)
    new_str = new_str.replace(' \n', '\n')
    print(new_str)

# conv('जीवन हुरीको गीत हो भने जसरि पनि गाउनै पर्छ सुखी मिलेन भने हामी दुखि दुखि नै मिल्नुपर्छ')
# conv('मेरा घरहरु गिर्छन्')
# conv('तर मायाले')
conv('''ति
तर मायाले''')
# conv('''[ऋतुहरुमा तिमी, हरियाली बसन्त हौ।
# नदीहरुमा तिमी हो, पबित्र गंगा हौ।]…२
# 
# [निर्दोष छन ति तिम्रा, हत्केलाहरू।
# तर मायाले भरिएका छन औलाहरु।]…२
# पवित्र छन तिम्रा, लाजका गहना। …२
# तर चाहनाले भिजेका छन, ओठहरु।
# 
# हावाहरुमा तिमी, शितल पवन हौ।
# नदीहरुमा तिमी हो, पबित्र गंगा हौ।
# 
# [प्रकृतिले मलाई जन्म दिएकी,
# तिम्रो सिउदो मा सिन्दुर भर्न।]…२
# सरस्वतीले कलम थमाए कि।…२
# तिम्रो सुन्दरताको सधैँ, बयान गर्न।
# 
# फूलहरुमा तिमी, कोमल गुलाव हौ।
# नदीहरुमा तिमी हो, पबित्र गंगा हौ।
# 
# ऋतुहरुमा तिमी, हरियाली बसन्त हौ।
# नदीहरुमा तिमी हो, पबित्र गंगा हौ।''')
# 
