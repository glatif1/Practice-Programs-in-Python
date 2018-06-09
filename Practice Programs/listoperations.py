








def create():
	userlist = []
	useradd = 0
	while useradd != "-1":
		useradd = input("Enter a value to add to list or Enter -1 to quit:")
		if useradd != "-1":
			userlist.append(useradd)
	return userlist








def inlist(item):
	if item in userlist:
		print("Yes! It's in the list.")
			
	else: 
		print("No! It's not in the list.")
#inlist(item)



def index(item):
	counter=0
	if item in userlist:
		while item != userlist[counter]:
			counter +=1
	else:
		print("It's not in the list!")
		print("")

	print("At index:",counter)

#index(item)

def remove(item):
	newlist = []
	counter = 0
	while item != userlist[counter]:
		counter +=1
	i= -1
	while i < counter-1:
		i+=1
		newlist.append(userlist[i])

	i = counter
	while i != len(userlist)-1:
		i += 1
		newlist.append(userlist[i])

	print(newlist)
#remove(item)


def insert(item,index):
	newlist=[]
	i= -1
	while i < index-1:
		i+=1
		newlist.append(userlist[i])

	newlist.append(str(item))

	i = index-1
	while i != len(userlist)-1:
		i += 1
		newlist.append(userlist[i])
	print(newlist)
#insert(item,index)

def join(list1):
	newlist= userlist+list1
	print(newlist)

print("")
print("You must create a list first!")
print("")

#the user creates a universal list
userlist = []
useradd = 0
while useradd != "-1":
	useradd = input("Enter a value to add to list or Enter -1 to quit:")
	if useradd != "-1":
		userlist.append(useradd)
print(userlist)

response = 1
while response != 2:
	


	#the menu
	print("""What would you like to do?
		

		1. Search List
		2. Search List for index value
		3. Insert Item
		4. Join two lists 
		5. Veiw list. It's too far up to scroll!
		6. Exit
		""")

	

	userinput = int(input("Enter corresponding number:"))

	if userinput == 1:
		item = input("Enter value to search:")
		inlist(item)
		response = int(input("Enter 1 to continue or 2 to exit:"))
	if userinput == 2:
		item = input("Enter value to search:")
		index(item)
		response = int(input("Enter 1 to continue or 2 to exit:"))
	if userinput == 3:
		item = input("Enter value to input in list:")
		index = int(input("Enter Index to input at:"))
		insert(item,index)
		response = int(input("Enter 1 to continue or 2 to exit:"))
	if userinput == 4:
		print("You will make a new list to add to the old one.")
		print("")
		userlist2= []
		useradd = 0
		while useradd != "-1":
			useradd = input("Enter a value to add to list or Enter -1 to add the lists:")
			if useradd != "-1":
				userlist2.append(useradd)
		print(userlist2,"This list will be appended to the existing")
		join(userlist2)
		response = int(input("Enter 1 to continue or 2 to exit:"))
	if userinput == 5:
		print(userlist)
		response = int(input("Enter 1 to continue or 2 to exit:"))
	if userinput ==6:
		response = 2

