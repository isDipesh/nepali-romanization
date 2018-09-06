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
CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब',
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
    # आज
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
        if char in BINDUS and idx > 0 and word[idx - 1] in KARS:
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


def conv(str):
    pattern = r'[^\s,!\?\[\]\(\)।]+'
    new_str = re.sub(pattern, handle_matches, str)
    new_str = new_str.replace(r' ।', ".")
    new_str = new_str.replace(r'।', ".")
    print(new_str)


# 
# conv('जीवन हुरीको गीत हो भने जसरि पनि गाउनै पर्छ सुखी मिलेन भने हामी दुखि दुखि नै मिल्नुपर्छ')
# conv('मेरा घरहरु गिर्छन्')
# conv('तर मायाले')
# conv('''ति 
# तर मायाले''')
# conv('''भेट भयो आज हामी सिन्डिकेट्को माझ हामी 
# उभिएछु तिम्रो बगल मा, बिजि तिमी मोबाइल मा हेरेछु 
# खेलेको योवन, 
# 
# नाम तिम्रो थाहा छैन तर मलाई पर्वाहा छैन 
# बोली केही रहेछौ है, आँखाले केही भनिरहेछौ है 
# बोलु त के भनेर 
# डर पनि लाग्छ सोचेर 
# 
# तिमी जाने सिलिगुरि, म जाने सिक्किम तिर 
# 
# खुसी छु है तिम्रै माझ भुले सारा संसार आज 
# तिमी पनि म संग नै जान भए कति रमाइलो 
# हुने थियो भन्नत 
# 
# कस्तो यो मिलन हाम्रो, बीस मिनेट को सम्बन्ध हाम्रो 
# पाएर पनि नपाए जस्तो, चिनेर पनि न चिने जस्तो 
# जिन्दगी यस्तै नै हो र 
# आफ्नै बाटो त जानू छदै छर 
# 
# तिमी जाने सिलिगुरि, म जाने सिक्किम तिर 
# 
# मलाई नै हेरेको झै लाग्छ घरी घरि 
# (हेरे लाग्छ घरिघरि) 
# फर्की हेर्छु म पनि आशा सरि 
# (हुउ... आशा सरि) 
# मनमा सोच्दै म रमाउद छु 
# (मनमा सोच्दै म रमाउद छु) 
# तिमी संगै भएको कल्पना गर्छु 
# (कल्पना गर्छुउ...) 
# 
# कस्तो धर्के पानी पर्यो, भिजेर म चुर भए 
# तिमी संगै ओत लागि आफ्नो गाडी पर्खिरहे 
# भिजेछु आज म रहर ले 
# 
# सबै गाडी चद्न थाल्यो कमाण्डर को हर्न सुनी 
# कलिम्पोङ टु सिलिगुरि, भन तिमी कस्तो निस्ठुरी 
# चडेर गयो कता तिर 
# छाडी राख्यौ मलाई यतै तिर 
# तिमी जाने सिलिगुरि, म जाने सिक्किम तिर 
# तिमी जाने सिलिगुरि, म जाने सिक्किम तिर 
# तिमी जाने सिलिगुरि, म जाने सिक्किम तिर
# ''')
# #

conv('''
उक्त परिवर्तन पटक छत लाञ्छना रहेछ समय यस्तो सहयोग समूह
कस्तो कस् चर्चा सदस्य झन् महँगो सँग तँ संयोजक प्रशंसा सङ्गठन अङ्ग
परिवर्तन उक्त सुन्दर बन्द, ध बन्धन सम्बन्ध, न जर्नल संलग्न, र प्रयोग मात्र, व स्वर पूर्व ह चिन्ह.
सम्म  टिप्पणी निर्णय नम्बर
कण्ठ, ड in खण्ड, ण in पूर्ण and उत्तीर्ण, न in प्रश्न, व in विश्व, श in आदर्श and स्पर्श, ट in कष्ट, प in पुष्प, ष in वर्ष and हर्ष. च in पञ्च and ज in कुञ्ज  मञ्च  च
गुरुङ रङ
अनुभव
''')
#
