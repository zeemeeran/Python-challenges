import requests

api_key = "da7744f48b38cebb38bbd8981cef0e46"
city = "New York"
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
#url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()
print(json) 
