# hackerRank problem 
# receive an input string with lower case alphabets and numbers
# output string should have all numbers and alphabets not present in the input string
# odered in ascending order with numbers first followed by alphabets

def missingCharacters(s):
    n = ['0','1','2','3','4','5','6','7','8','9']
    ch = ['a', 'b', 'c', 'd','e', 'f','g', 'h','i', 'j', 'k', 'l', 'm','n','o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    temp = ''
    temp1 = ''.join(n)
    temp2 = ''.join(ch)
    temp = temp1 + temp2
    print(temp)

    for i in s:
        temp = temp.replace(i, '')
        
    print(temp)

    return temp


result = missingCharacters('8hypotheticall024y6wxz')

print(result + '\n')


