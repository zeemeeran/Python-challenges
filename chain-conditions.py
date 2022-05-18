# chain conditions

a = 10

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
