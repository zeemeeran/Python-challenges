"""
Write a Python script to:

    Display all the prime numbers between 1 to 250.
    Store the results in a results.txt file.
    Author - Zahida Meeran
"""
import os

# function to check if a number is prime

def isPrime(num):
    i = 2
    while i <= num-1 :
        if num % i == 0 :
            print(f'Not prime: {num}')
            return False
        else :
            i = i+1
    else :
        print(f'Prime: {num}')
        return True
        
# creating a new file Zee-results.txt

os.system('touch Zee-results.txt')
os.system('echo "List of prime numbers from 1 to 250: " > Zee-results.txt')

#opening file Zee-results in append mode
fprime = open("Zee-results.txt", 'a')

primeCount = 0

# checking for prime numbers between 2 and 250

for num in range(2,251):
    if isPrime(num):
        primeCount += 1
        fprime.write("\n" + str(num))
    
fprime.write("\n" + "Total number of prime numbers betweeen 1-250 is : " + str(primeCount))
fprime.close()

        