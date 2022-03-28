#hoursWorked = float(input('Enter Hours: '))
hoursWorked = input('Enter Hours: ')
rate = input("Enter rate: ")

try :
    hrWrkfl = float(hoursWorked)
    flrate = float(rate)
except :
    print('Error, enter numeric input')
    quit()

if  hrWrkfl > 40 :
    othrs = hrWrkfl - 40 
    otpay = othrs * 1.5 * flrate
else :
    otpay = 0

pay = 40 * flrate
totalpay = pay + otpay
print("The pay is: ", totalpay) 