# check if a sentence has a space
# method 1 - using find

sentence = "Ilovepython"

print(sentence.find("\t"))

if sentence.find('\t') != -1 :
    print("Sentence has tab")
elif sentence.find(" ") != -1:
    print("Sentence has space")
else:
    print("No space")


# method 2
def isSpace(sen):
    for i in sen:
        if i == '\t' :
            return "tab"
        elif i == ' ':
            return "space"
    else :
            return "nospace"

        
if isSpace(sentence) == "tab":
    print("sentence has tab!")
elif isSpace(sentence) == "space":
    print("sentence has space!")
else :
    print('Sentence has no space or tab!')

    
def isSpace2(sen):
    if ' ' in sen or '\t' in sen:
        return True
    else :
        return False

if isSpace2(sentence):
    print("Space exists!")
else:
    print('no space!!!')