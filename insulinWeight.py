
# Store the human preproinsulin sequence in a variable called preproinsulin:

preproinsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin
print('count of c in aInsulin is : ' , aInsulin.count('c'))

# Printing "the sequence of human insulin" to console using successive print() commands:

print("The sequence of human preproinsulin is : ")
print(preproinsulin)

# Printing to console using concatenated strings inside the print function (one-liner):

print("The sequence of human insulin - chain a is : " + aInsulin)

# Calculating the molecular weight of insulin  

# Creating a list of the amino acid (AA) weights  

aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 

# Count the number of each amino acids  

aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  

print('\ncount of insuliin: ')
print(aaCountInsulin)

molWtInsulin = {x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}

# print(tempdic)

print("\nPrinting tempdic :" , molWtInsulin)

print("\nPrinting values of tempdic : ", molWtInsulin.values())

molecularWeightInsulin = sum(molWtInsulin.values())

print("\nprinting molecular wt by using a temp dic : " , molecularWeightInsulin)

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  


print("The rough molecular weight of insulin rounded : " + str(round(molecularWeightInsulin, 2)))

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63

print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

print("Error percentage rounded: " + str(round((((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100), 2)))

