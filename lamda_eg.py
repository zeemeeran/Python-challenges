

# basic lambda with 2 arguments

lmdfn = lambda x, y : x + y

print(lmdfn(5,7), "\n")

# lambda fn with no arguments
x = lambda : "hello world"

print(x(), "\n")

#lambda with nested lambda functions

higher_order = lambda x, lamdafn : x * lamdafn(x)

print(higher_order(10, lambda x : x * x), "\n")

# lambda invocation as it is defined

#z = (lambda x,y : (x+y)*10)(5,8)
# print(z, "\n")

print((lambda x,y : (x+y)*10)(5,8))


# Using lambda inside filter function
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list(filter(lambda x : (x%2==0), list1))
print(list2, "\n")

list3 = list(map(lambda x : x%2, list1))
print(list3)


from functools import reduce
sum = reduce((lambda x,y: x+y), list1)
print(sum)
