# enumerate function and objects

grades = [ 3.5, 2.75, 4.2, 3.9]

print("Printing grades")
for grade in grades:
    print(grade)

e_grades = enumerate(grades)

print("e_grades", e_grades)

print("looping e_grades")
for index, grade in e_grades:
    print(index, grade)

print("looping using enumerate function")
for index, grade in enumerate(grades):
    print(index, grade)