number = 0
large = 0
small = 100000000000
while number != -1:
	number = int(input("Please enter a number or -1:"))

	if number > large:
		large = number
	if number < small:		
		if number != -1:
			small = number



print("Large:",large)
print("Small:",small)
