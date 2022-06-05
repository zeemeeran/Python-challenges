strings = ['food', 'bar', 'baz', 'bread', 'apples']

strings.sort()
print(strings)

strings.sort(key=lambda s: len(s))
print(strings)
