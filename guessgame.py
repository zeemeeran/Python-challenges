"""
guessing game
"""
import random

print("Enter a number to see u guessed it right!")

import random

num = random.randint(1,10)
#print(num)

isGuess = False

while isGuess != True :
    guess = input("Enter your guess: ")
    if int(guess) == num :
        print("{} is the right guess" .format(guess))
        isGuess = True
    else :
        print("Sorry {} is a wrong guess, try again" .format(guess))
        
