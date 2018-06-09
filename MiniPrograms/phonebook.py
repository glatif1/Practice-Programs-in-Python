def showmenu():




def main():
	contacts = {}
	continueYorN = "Y"

	while continueYorN =="Y":
		userchoice = showMenu()

		if userchoice ==1:
			name= input("Enter the name:")
			phonenum = input("Enter the phone number: ")

			contacts[name]=phonenum

		elif userchoice ==2:
			print(contacts)
		else:
			print("Invalid Input")

		continueYorN = input("Continue(Y/N)?")