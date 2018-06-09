base = int(input("Enter the base:"))
exponent = int(input("Enter the exponent:"))
result = 1
while exponent > 0:
	result = result*base
	exponent = exponent - 1 
print(result)
