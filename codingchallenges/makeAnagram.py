# remove characters in string to make them anagrams

string1 = "raced"
string2 = "caressed" 

def removeChar(st1, st):
    temp =""
    for i in st1:
        if i in st:
            temp += i
            st = st.replace(i, '')
            
    return temp


if set(string1) <= set(string2):
    print("anagram")
    temp = removeChar(string2, string1)
    string2 = temp
    
elif set(string2) <= set(string1):
    print("str2 in string1 anagram")
    temp = removeChar(string1, string2)
    string1 = temp
else:
    print("not anagram")

print(f'string1 = {string1}, string 2 = {string2}')




