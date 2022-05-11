a = 10 
b = 20
a,b = b,a
print(a,b) 

a,b,c = 10,1.7,'Hello World'
print(a,b,c) 

if 3 < 2:
    var=21
else:
    var=42

var = 21 if 3<2 else 42

#elif

x = 42
if x > 42:
    print("no")
elif x == 42:
    print("yes")
else:
    print("maybe")


print("no") if x > 42 else print("yes") if x == 42 else print("maybe")


#If without else

morning = True

if morning:
    print('Good Morning!')

if morning: print('Good Morning!!')

print('Good Morning...') if morning else None
