"""
Your module description
"""

import json



def readJsonFile(filename):
    data = ""
    
    try :
        with open(filename, 'r') as json_file :
        #json_file = open(filename)
            data = json.load(json_file)
    except IOError :
        print("Cannot open file")
        
    #print(data)
    return data
        
        
        
# readJsonFile(/home/ec2-user/environment/insulin.json)
#readJsonFile("insulin.json")


