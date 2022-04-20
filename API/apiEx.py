import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
#This returns a JSON object with TODO's structured like so:

todo = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}

print(todos)