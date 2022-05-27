#print index of numbers that sum to 12 in the array

numArr = [9, 7, 3, 12, 18, 5]

for num in numArr:
    for num2 in numArr:
        if (num + num2) == 12:
        # Element 9 has index [0]
            print(f'Element {num} has index {numArr.index(num)}', end = " & ")
            print(f'Element {num2} has index {numArr.index(num2)}')
