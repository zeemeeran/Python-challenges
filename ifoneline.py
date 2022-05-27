
if 1 < 2:
    x='yes..'
else:
    x='no'
#print(x)

x='yes!!' if 3 < 2 else 'no!!!'
print(x)


#elif
x = 1
if x > 1:
    print("no")
elif x == 1:
    print("yes x is 1")
else:
    print("maybe")


print("no") if x > 1 else print("yes") if x == 1 else print("maybe")


#If without else
morning = True

if morning:
    print('Good Morning!')

if morning: print('Good Morning!!')

print('Good Morning...') if morning else None