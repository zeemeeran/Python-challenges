
word = input("Enter a word: ").upper()
vow = ('A','E','I','O','U')
new = ""
for i in word :
    if i not in vow:
        new += i

print(new)

import re

print(re.sub("[AEIOU]", "" , word))


    


