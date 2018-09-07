Romanization of Nepali Unicode
========================== 

This is a Python script to phonemically transcript Nepali text or words in Devanagari script to Latin Script.

## Usage:

```
from romanize import romanize_text, romanize_word

print(romanize_text('''
(यस्तो पनि हुँदो रहेछ जिन्दगीमा कहिले कहिले 
कसैलाई माया गर्ने एउटा भूल गरें मैले 
यस्तो पनि हुँदो रहेछ...)२ 

मेरो जस्तो माया दिने तिमीलाई हजार होला 
तिम्रो लागि मेरा जस्ता हजार हजार मुटु रोला 
जस्लाई आफ्नो सम्झेको थिएँ उहि बिरानो भयो अहिले 

कसैलाई माया गर्ने एउटा भूल गरें मैले 
यस्तो पनि हुँदो रहेछ... 

मेरो माया कुल्चि जाने तिम्रो माया फलोस् फुलोस् 
मेरो इच्छा मारी जाने तिम्रो इच्छा सधैं नै पुगोस् 
उदास आँखा मेरा पनि सपना देख्थे पहिले पहिले 
कसैलाई माया गर्ने एउटा भूल गरें मैले 
यस्तो पनि हुँदो रहेछ...
'''))
# Lyrics Credit: Yadav Kharel

print(romanize_word('मत्स्येन्द्रनाथ'))
``` 

The above script would output
```

(yasto pani hundo rahechha jindagima kahile kahile 
Kasailai maya garne euta bhul gare maile 
Yasto pani hundo rahechha...)2 

Mero jasto maya dine timilai hajar hola 
Timro lagi mera jasta hajar hajar mutu rola 
Jaslai aaphno samjheko thie uhi birano bhayo ahile 

Kasailai maya garne euta bhul gare maile 
Yasto pani hundo rahechha... 

Mero maya kulchi jane timro maya phalos phulos 
Mero ichchha mari jane timro ichchha sadhai nai pugos 
Udas aankha mera pani sapana dekhthe pahile pahile 
Kasailai maya garne euta bhul gare maile 
Yasto pani hundo rahechha...

matsyendranath
```

## Note:
 - The script was developed to transcript Nepali text for targeting search keywords by general users. Therefore, the script tries to convert to what a general user would type a given Nepali word in Latin script. For example, 'गरें' is converted to 'gare' while 'garen' being the phonemically correct transcription.
 - The transcripted script isn't always accurate, specially where it needs to decide on the pronounciation of inherent vowels. For example, 'दिन' can either be 'din', meaning 'day'; or 'dina', meaning 'to give'.     
- Words in new line and those after punctuation characters are automatically capitalized.

--------------------------------------

Contributions are welcome, espesically the use of intelligence for pronounciation of inherent vowels :).
 
