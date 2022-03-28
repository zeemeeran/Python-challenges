
wt = input('Weight: ')
unit = input('(L)bs or (K)g: ')

try :
    fl_wt = float(wt)
except :
    print("Invalid weight")
    quit()

if unit == 'l' or unit == 'L' :
    wt1 = fl_wt/2.2
    unit = 'kilograms'
elif unit == 'k' or unit == 'K' :
    wt1 = fl_wt * 2.2
    unit = 'pounds'
else :
    print("Invalid entry")

print(f'You are {wt1} {unit} !')
