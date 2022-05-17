## list of dictionaries
dicts = [
   {"name" : "John", "salary" : 10000},
   {"name" : "Emma", "salary" : 30000},
   {"name" : "Harry", "salary" : 15000},
   {"name" : "Aslan", "salary" : 10000}
]

## sorting the above list using 'lambda' function
## we can reverse the order by passing 'reverse' as 'True' to 'sorted' method
print(sorted(dicts, key = lambda item: item['salary']))