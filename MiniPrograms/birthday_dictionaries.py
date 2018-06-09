i = "y"
birthdays = {'me':'1/27','you':'6/8'}
while i == 'y':
	
	name = input("Enter Name to search/add to dictionary: ")

	if name in birthdays:
		print("The birthday: ", birthdays[name])
	else:
		print("Not found!" )
		
		bdate = input("Enter the birthday: ")
		birthdays[name]=bdate
	i = input("Enter y to continue or n to quit:").lower()
	print(birthdays)
