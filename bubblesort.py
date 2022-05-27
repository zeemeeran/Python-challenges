narr = [6, 4 , 9, 2, 7, 5]
print(narr)
for i in range(0,len(narr)-1):
    for j in range(i+1, len(narr)):
        if narr[i] > narr[j]:
            narr[i], narr[j] = narr[j], narr[i]

print(narr)