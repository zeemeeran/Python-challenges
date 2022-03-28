
#phone number in words

numWord = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']

num = input("Enter your phone number: ")

for i in num:
    print(numWord[int(i)], end=" " )

digit_mapping = {
    '1':'one', '2':'two', '3':'three', '4':'four', '5':'five'
}

output = ""
for i in num:
    output += digit_mapping.get(i, "!") + " "

print(output)