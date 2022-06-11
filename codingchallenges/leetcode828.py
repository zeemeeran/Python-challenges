# leetcode 828. Count Unique Characters of All Substrings of a Given String

# Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
# For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
# Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.
# Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

# Example 1:

# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Every substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

# Example 2:
# Input: s = "ABA"
# Output: 8
# Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

# Example 3:
# Input: s = "LEETCODE"
# Output: 92

def countUniqueChar(s):
    char_seen = []
    for i in s:
        if i not in char_seen:
            char_seen.append(i)
        else:
            char_seen.remove(i)
            s.replace(i,'')
    return len(char_seen)

st = 'Love'

# substringlist = [st[i:j] for i in range(len(st))
#                 for j in range(i+1, len(st) +1)]


# slist = []

# for index, ch in enumerate(st):
#     for i in range(index + 1, len(st)+1):
#         slist.append(st[index:i])

sl =[]
st1='LEETCODE'
for i in range(len(st1)):
    for j in range(i+1, len(st1) +1):
        sl.append(st1[i:j])

# print(substringlist)
# print(slist)
#print(sl)
x =0
sum = 0
for i in sl:
    x = countUniqueChar(i)
    print(i, x)
    sum += x

print(sl, sum)

