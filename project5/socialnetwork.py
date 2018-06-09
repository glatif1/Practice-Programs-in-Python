from person import Person
import pickle
file = open('network.txt', 'r')

userlist = []
usernamelist = []
friendslist=[]

for i in file.readlines():
	i = i.split(',')
	pobj = Person(i[0],i[1],i[3],i[5])
	userlist.append(pobj)
	usernamelist.append(i[0])
	friendslist.append(i[5])

file2 = open('network2.txt', 'a')

j =0

exit = True
while exit:
	username = input('Enter Username:')
	username = username.lower()
	for i in userlist:
		if username in i.getusername():
			password = input("Enter Password:")

			while password == i.getpassword():
				print("""What would you like to do? :
					1. Print all my friends
					2. Print Messages 
					3. Post Message
					4. Add Friend 
					5. Print all my friends' messages
					6. Logout 
					7. Exit """)
				response = int(input("Enter the corresponding number:"))
				if response ==1:
					print(i.getfriends())
				if response == 2:
					print(i.getmessages())
				if response ==3:
					print(i.getmessages())
				if response == 4:
					addfriend= input("Enter the friends name:")
					if addfriend in usernamelist:
						temp = i.getfriends()
						new = temp+addfriend
						i.setfriends(new+":")
						print(i)
						with open('network2.txt', 'ab') as d:
							pickle.dump(i,d)
						with open('network2.txt', 'r') as f:
							i = pickle.load(f)
					
				if response == 5:
					for j in userlist:
						if j.getusername() in i.getfriends():
							print(j.getmessages())

				if response == 6:
					password = "null"
				if response == 7:
					exit == False
			else:
				print("incorrect password")

file2.close()






