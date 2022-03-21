

price = 1000000
try :
    buyer_credit = input('Is buy credit good : y/n : ')
except :
    print('Enter proper answer')

if buyer_credit == 'y' :
    print(f'Buyer needs to downpay ${price/10}')
elif buyer_credit == 'n' :
    print(f'Buyer needs to downpay ${price*2/10}')
else :
    print('Not valid option')
