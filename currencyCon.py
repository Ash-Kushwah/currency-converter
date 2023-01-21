with open('convertData.txt') as f:
    lines = f.readlines()

currencyDict = {}

for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]


amount = int(input("Enter the amount: "))
print("Enter the name of currency you wang to convert to. \n")
[print(item) for item in currencyDict.keys()]

currency = input("Paste one of the above values: ")
print(f"{amount} INR = {amount*float(currencyDict[currency])} {currency}")
