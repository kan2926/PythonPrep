# -*- coding: utf-8 -*-
import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)

morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
                      ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
                      ".--","-..-","-.--","--.."]
morse_dict = dict(zip(string.ascii_lowercase, morse_code))

print(morse_dict)
resultset = set()
morse_words_list = ['gin','zen',  "gig", "msg"]
for word in morse_words_list:
    temp = ''
    for i in word:        
        temp += morse_dict[i]
    print(word,'--->',temp)
    resultset.add(temp)
    
print(resultset)