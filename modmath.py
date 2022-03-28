
import math

try :
    x = float(input("Enter a decimal number: "))
except :
    print("Not a valid number!")
    quit()
    
print("Math fab of {} is {}!" .format(x,math.fabs(x)))
print("Math floor of {} is {}!" .format(x,math.floor(x)))




