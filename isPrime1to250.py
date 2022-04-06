"""
Write a Python script to:

    Display all the prime numbers between 1 to 250.
    Store the results in a results.txt file.
"""
import os
import subprocess


def isPrime(num):
    i = 2
    while i <= num-1 :
        if num % i == 0 :
            print(f'Not prime: {num}')
            return False
        else :
            i = i+1
            continue
    else :
        print(f'Prime: {num}')
        return True
        
print(isPrime(1))

os.system('touch results.txt')
os.system('echo "List of prime numbers from 1 to 250: " > results.txt')
fprime = open("results.txt", 'a')

primeCount = 0

for num in range(2,251):
    if isPrime(num):
        primeCount += 1
        fprime.write("\n" + str(num))
    
fprime.write("\n" + "Total number of prime numbers betweeen 1-250 is : " + str(primeCount))
fprime.close()

        
    