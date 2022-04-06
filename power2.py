
# check if a given positive integer is a power of two.

num = int(input("Enter a positive number: "))
saveNum = num 

# first method using loop

if num == 1:
    print('2 to the power of 0 is 1, so yes 1 is a power of 2!!')
else:
    while num/2 != 1 :
        if num % 2 != 0 :
            print(f'{saveNum} is not a power of 2!')
            break
        else :
            num = num / 2
    else :
        print(f'{saveNum} is a power of 2!!')


import math

# another way to find if a number is a power of 2 in a single statement
# if the result of this  expression math.log10(num)/math.log10(2) is 
# a whole number, it is a power of 2
# using is_integer to see if it is a whole number


print(f'Using ternery operator/log function --> {saveNum} is', ("not a power of 2", "a power of 2")[(math.log10(num)/math.log10(2)).is_integer()])

