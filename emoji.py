

def emoji_builder(msg) :
    emoji = {
        ":)": "😊",
        ":(": "😒😥"
    }

    words = msg.split(" ")
    output = ""

    for word in words :
        output += emoji.get(word, word) + " "

    return output

msg = input('>> ')
output = emoji_builder(msg)
print(output)