checking = saving=0
while checking >=0 and saving>=0:
	checking = int(input("Enter initial chackings amount:"))
	saving = int(input("Enter the initial savings amount:"))
	print("""What would you like to do?

		1. Deposit
		2. Withdrawal
		3. Transfer
		
		""")
	a=input("Please enter the word:")
	usertrans= a.lower()
	print("For which account? Checkings or Savings")
	b=input("Please enter:")
	useraccount=b.lower()
	if usertrans=='deposit' and useraccount=='checkings':
		userdeposit=int(input("Enter the amount to deposit to your Checking account:"))
		checking=checking+userdeposit
	if usertrans=='withdrawal' and useraccount=='checkings':
		userwithdrawal=int(input("Enter how much to withdraw from your Checking account:"))
		checking=checking-userwithdrawal
		if checking <0:
			print("Checkings Overdrawn!")
	if usertrans =='transfer' and useraccount=='checkings':
		usertransfer=int(input("Enter the amount to transfer from Checkings to Savings:"))
		checking= checking-usertransfer
		if checking<0:
			print("Checkings Overdrawn!")
		saving=saving+usertransfer
	if usertrans=='deposit' and useraccount=='savings':
		userdeposit=int(input("Enter the amount to deposit to your Saving account:"))
		saving=saving+userdeposit
	if usertrans=='withdrawal' and useraccount=='savings':
		userwithdrawal=int(input("Enter how much to withdraw from your Saving account:"))
		saving=saving-userwithdrawal
		if checking <0:
			print("Savings Overdrawn!")
	if usertrans =='transfer' and useraccount=='savings':
		usertransfer=int(input("Enter the amount to transfer from Savings to Checkings:"))
		saving= saving-usertransfer
		if saving<0:
			print("Savings Overdrawn!")
		checking=checking+usertransfer
	print("Final Checking:",checking,"Final Savings:",saving)




