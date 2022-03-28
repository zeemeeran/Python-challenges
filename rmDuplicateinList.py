
num = [2, 6, 8, 54, 23, 14, 76, 100, 6, 23, 100, 54 , 43, 10, 20, 2, 77, 200, 100, 29, 20, 56, 10, 45, 34, 54, 100]

print(num)

for i in range(0,len(num)):
    for j in range(i+1, len(num)):
        try:
            if num[i] == num[j] :
                num.remove(num[j])
        except IndexError:
            break
    
print(num)


num = [1, 2, 5, 2, 4, 5, 8, 1 ]
uniques = []
print(num)

for i in num :
    if i not in uniques :
        uniques.append(i)
print(uniques)