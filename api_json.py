import pip._vendor.requests

#response = pip._vendor.requests.api.get("https://api.open-notify.org/astros.json")
#print(response)

r = pip._vendor.requests.api.get('https://www.dataquest.io/')
print(r)

print(type(r))

#url = 'http://httpbin.org/json'
#r = pip._vendor.requests.api.get(url)
#print('Response Code:', r.status_code)
#print('Response Headers:\n', r.headers)
#print('Response Content:\n',r.text)

#print(r.headers['Content-Type'])
#print(r.text[123])


url = 'http://httpbin.org/get'
payload = {
    'website':'dataquest.io',
    'courses':['Python','SQL']
    }
r = pip._vendor.requests.api.get(url, params=payload)
print('Response Content:\n',r.text)

