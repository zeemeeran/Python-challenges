print(("Not a power of 2", "Is a power of 2")[(math.log10(num)/math.log10(2)).is_integer()])

functions = (func,func2)

def func():
    print("1")

def func2():
    print("2")

functions[3 > 2]()
