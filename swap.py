# swap variables

a = 10 
b = 20
print(a,b)

a,b = b,a
print(a,b) 

a,b,c = 10,1.7,'Hello World'

print(a,b,c) 

# chain conditions

if 20 > a > 5:
    print("chain conditions1 true")

if 20 < a > 5:
    print("chain condition2 true")
else:
    print("chain condition2 false")

# function returns multiple values
def fun():
    return 100, True

x, success = fun()
print(f'x = {x} \nsuccess = {success}')

