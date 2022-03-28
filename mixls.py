"""
Mixed list
"""

mixls = [45, "55", 72.45, True, "hello", False, 5j, 100, 3.14]

print(mixls)
print(type(mixls))

for item in mixls :
    print("{} is of type {}" .format(item, type(item)))
