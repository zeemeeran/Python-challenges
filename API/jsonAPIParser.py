'''

Welcome to 'Challenge Activity' 6.4.14.c01! This challenge
activity is going to test your comprehension on parsing
JSON data and interacting with the user. Here are the requirements 
for your JSON program for this Challenge Activity:

1. The program must run until the user decides to quit
2. Your list program needs to support the following user options:
    a. Provide a cryptocurrency price quote leveraging the LunarCrush API
    b. Provide directions leveraging the MapQuest API
    c. Provide an alphabetically sorted list (by first name) of all
       the astronauts currently in space using the ISS API
    d. Allow the user to quit

Once you have completed this activity you can 'Submit' your file and
view one possible solution set for the activity or you can 'Fork'
the solution set to have a copy with which you can work. If you look
at the image to the left, 6.4.14.c01-image you will see an 
example of what your menu could look like and how some of the 
functionality should work.

Good luck and here are some import statements to get you started!

'''
'''
Welcome to my Json Parsing Program!
Would you like to:
1. Get a crypto quote
2. Get directions using MapQuest
3. Get a list of astronauts in space sorted alphabetically
4. Quit

Your choice: 3

Here is a list of the astronauts currently in space sorted alphabetically by first name:

The astronauts currently in space are:
'''
from requests import get
from urllib.parse import urlencode

print("Welcome to my Json Parsing Program!")
options = '''Would you like to:
            1. Get a crypto quote
            2. Get directions using MapQuest
            3. Get a list of astronauts in space sorted alphabetically
            4. Quit'''

print(options)

# User Defined functions
def user_choice():
  print()
  userInput= input("Your choice: ")
  print()
  return userInput

def getURI(uri):
  responseObject = get(uri)
  jsonData = responseObject.json()
  return jsonData

def getCryptoPrice():
  symbcrypto= input("Please enter a cryptocurrency symbol, BTC, ETH e.t.c. : ").upper()
  jsonData= getURI("https://api.lunarcrush.com/v2?data=assets&key={API_KEY_HERE}&symbol=" + symbcrypto)
  tokenSymbol = jsonData["data"][0]["symbol"]
  tokenPrice = jsonData["data"][0]["price"]
  print()
  print("The current price of " + tokenSymbol + " is: $" + str(tokenPrice))
  print()

def getMapDirection():
  tripStartingLocation= input("Enter the starting address of your trip: ")
  tripEndingLocation= input("Enter the address of your ending location: ")
  uriMapQuest= 'http://www.mapquestapi.com/directions/v2/route?'
  keyMapQuest = 'NGMJMoREO5aShAzbLtLChdPpxGVbuLQd'
  uriEncoded= uriMapQuest + urlencode({"key": keyMapQuest, "from":tripStartingLocation, "to":tripEndingLocation})
  jsonData= get(uriEncoded).json()
  print(jsonData['route']['distance'])
  print(jsonData['route']['legs'][0]['destNarrative'])
  print(jsonData['route']['legs'][0]['origNarrative'])
  for distIndx in range(len(jsonData['route']['legs'][0]['maneuvers'])):
    print(jsonData['route']['legs'][0]['maneuvers'][distIndx]['narrative'])
  
def getAstronautsList():
  jsonData= getURI("http://api.open-notify.org/astros.json")
  astronautNames= []
  
  for i in range(len(jsonData['people'])):
    astronautNames.append(jsonData['people'][i]['name'])
  print("Here is a list of the astronauts currently in space sorted alphabetically by first name: ")
  print()
  print("The astronauts currently in space are: ")
  print()
  astronautNames.sort()
  print("Here is an alphabetical list of all astronauts in space: ", astronautNames)
  print()

true = True
while true:
  response = user_choice()
  if response == "1":
    true = True
    getCryptoPrice()
    print(options)
  elif response == "2":
    true = True
    getMapDirection()
    print(options)
  elif response == "3":
    true = True
    getAstronautsList()
    print(options)
  elif response == "4":
    true = False
    print(options)
  else:
    true = True
    print("Sorry, wrong option.")
    
  if true == True:
    continue

print("Bye!")