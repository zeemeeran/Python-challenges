
# basic lambda with 2 arguments

lmdfn = lambda x, y : x + y

print(lmdfn(5,7))

# lambda fn with no arguments
x = lambda : "hello world"

print(x())

#lambda with nested lambda functions

higher_order = lambda x, lamdafn : x * lamdafn(x)

print(higher_order(10, lambda x : x * x))

# lambda invocation as it is defined

z = (lambda x,y : (x+y)*10)(5,8)
print(z)