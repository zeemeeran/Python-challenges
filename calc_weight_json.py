"""
Your module description
"""

import jsonFileHandler

data = jsonFileHandler.readJsonFile("insulin.json")

if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin 
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    print('bInsulin is : ', bInsulin)
    print('aInsulin is :', aInsulin)
    print('molecularWeightInsulinActual : ', str(molecularWeightInsulinActual))
    
    # Calculating the molecular weight of insulin  
    # Getting a list of the amino acid (AA) weights 
    
    aaWeights = data['weights']
    
    # Count the number of each amino acids  
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
    
    # Multiply the count by the weights  
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
    
    print("\n The rough molecular weight of insulin: " + str(round(molecularWeightInsulin, 2)))
    print("\n Percent error: " + str(round((((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100), 2)))
    
else :
    print("Error, exiting program....")