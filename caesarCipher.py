"""
Caesar Cipher encryption
"""
def getDoubleAlphabet(alpha) :
   # doubelAlpha = alpha + alpha
    doubelAlpha = alpha * 2
    return doubelAlpha

print(getDoubleAlphabet('Zee'))


# get message to be encrypted from the user

def getMessage() :
    strToEncrypt = input("Enter a message to encrypt: ")
    return strToEncrypt

#get the key(number to rotate) for encryption from user    
def getCipherKey() :
    shiftKey = input("Enter a key, whole number (1 -25) : ")
    return shiftKey
    
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# message = getMessage()
# cipherKey = getCipherKey()

# encryptedMessage = encryptMessage(message, cipherKey, alpha)

# print('\n Encrypted msg : ', encryptedMessage)

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
# decryptedMessage = decryptMessage(encryptedMessage, cipherKey, alpha)
# print('\n Decripted msg : ', decryptedMessage)


def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
  
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
  
    myMessage = getMessage()
    print(myMessage)
  
    myCipherKey = getCipherKey()
    print(myCipherKey)
  
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
  
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

    
runCaesarCipherProgram()