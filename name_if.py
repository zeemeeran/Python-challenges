
name = input('Enter name: ')

print(len(name))
namelen = len(name)

if namelen > 2 and namelen <= 50 :
    print("Name correct")
else :
    print("Name wrong")