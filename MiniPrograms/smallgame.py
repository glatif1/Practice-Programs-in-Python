from PIL import Image
win = False

while win == False:
	print("""
		Welcome to BOOSER CASTLE
	 	
	 	Choose a door to enter

		-----			
		| 	|
		| 1 |
		|	|	
		-----

		-----
		|	|
		| 2 |
		|	|	
		-----

		-----
		|	|
		| 3 |
		|	|	
		-----
		""")

	userdoor =input("Pick a door. Any door:")


	if userdoor=="1":
		print("You died!")
	if userdoor=="2":
		print("""You see two other doors!

	 	Choose a door to enter

		-----			
		|	|
		| 1 |
		|	|	
		-----

		-----
		|	|
		| 2 |
		|	|	
		-----
		""")
		userdoor2=int(input("Enter 1 or 2:"))
		if userdoor2 == 1 or userdoor2==2:
			print("""


				You fell into fire and died!


				""")
			image= Image.open('fire-vector.png')
			image.show()
		else:
			print("Read Instructions!")

		
	if userdoor=="3":
		print("""You see two other doors!

	 	Choose a door to enter

		-----			
		|	|
		| 1 |
		|	|	
		-----

		-----
		|	|
		| 2 |
		|	|	
		-----


		""")
		userdoor3=int(input("Enter 1 or 2:"))
		if userdoor3==1:
			print("Enter ")



