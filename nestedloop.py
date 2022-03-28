
num = [5, 2, 5, 2, 2]

num = [2, 2, 2, 2, 8, 8]

#for i in num :
#   for j in range(i) :
#        print('*', end='')
#        if j == i-1 :
#            print('\r')

for i in num :
    out =''
    for j in range(i) :
        out += '*'
    print(out)
    
        