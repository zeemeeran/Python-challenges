
import requests

print('Welcome to the Crypto Price Checker v2.0!')
print()

tokenList = [ ]

while True:

    print()
    print('Please choose from one of the options below: ')
  
    #added try except for invalid choice bug 1

    try:
        whatNext = int(input('1. Add new token to list\n2. View current token list\n3. Get current token pricing for all coins\n4. Get current token price for one (1) coin\n5. Quit\n\nYour selection: '))
    except ValueError: 
        whatNext = 0

    if whatNext == 1:
        print()
        userResponse = input('Please enter token symbol: ')
        tokenList.append(userResponse)
        print()
        print('Thank you! Your token has been added to the list!')
    elif whatNext == 2:
        print()
        if tokenList:
            print('The current list of tokens is: ', tokenList)
        else :
            print("Token list is empty") # added if else bug 5

    elif whatNext == 3:
        print()
        for token in tokenList:
            cryptoURI = "https://api.lunarcrush.com/v2?data=assets&key={API_KEY_HERE}&symbol="+token.upper()
            json_data = requests.get(cryptoURI).json()
            ## There are no errors on the next two (2) lines as we haven't covered
            ## JSON data and how to manipulate it using Python just yet...
            tokenSymbol = str(json_data["config"]["symbol"])

            # BUGBUG if invalid token in token list
            try:
                currentPrice = str(json_data["data"][0]["price"])
            except IndexError:
                print(f'{token} is not a valid token!\n')
                continue

            ## You might find errors below this line
            print('The price of ' + token.upper() + ' is: $' + currentPrice)
    elif whatNext == 4:
        #userResponse = input('Please enter token symbol: ') #---bug 2
        #tokenList.append(userResponse)

        print()
        singleToken = input('Enter token symbol: ')
        cryptoURI = "https://api.lunarcrush.com/v2?data=assets&key={API_KEY_HERE}&symbol="+singleToken.upper()
        json_data = requests.get(cryptoURI).json()
        ## There are no errors on the next two (2) lines as we haven't covered
        ## JSON data and how to manipulate it using Python just yet...
        tokenSymbol = str(json_data["config"]["symbol"])
        
        # if invalid token entered, catching indexerror exception as token not found in list  ---- bug
        try:
            currentPrice = str(json_data["data"][0]["price"])
        except IndexError:
            print("\nInvalid token!!")
            input()
            continue

        ## You might find errors below this line
        print('The price of ' + singleToken.upper() + ' is: $' + currentPrice)
    elif whatNext == 5:
        break
    else:
        print('\nYou did not make a valid choice. Try again!')
        input()

print()


#if tokenList exists then print, if given 5 exit in the beginning itself it prints empty list ---bug 3
if tokenList:
    print('Your final list of tokens was: ', tokenList)
print('Thank you for using my program!') #\ bug 4