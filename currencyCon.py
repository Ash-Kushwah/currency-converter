# Opening the file which contains all the currency exchange values 
with open('convertData.txt') as f:
    lines = f.readlines()

# Initializing an empty dictionary 
currencyDict = {}

# Formatting the data and sending it to the dictionary 
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

# Getting the amount from the user 
amount = int(input("Enter the amount: "))
# Printing the available options 
print("Which currency you wang to convert to. \n")
[print(item) for item in currencyDict.keys()]

# Getting the currency in which we want to convert
currency = input("Paste one of the above values: ")
# Printing the converted amount 
print(f"{amount} INR = {amount*float(currencyDict[currency])} {currency}")
