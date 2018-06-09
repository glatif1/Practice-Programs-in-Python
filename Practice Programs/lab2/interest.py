startbalance = float(input("Enter initial balance:"))
intrate = float(input("Enter annual interest rate:"))
years = int(input("Enter years:"))

if years == 0:
	print(startbalance)
else:
	while years > 0:
		addedinterest = startbalance * intrate
		newbalance = startbalance + addedinterest
		startbalance = newbalance
		years = years - 1
	print(newbalance)

