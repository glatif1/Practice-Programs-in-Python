useryear = int(input("Enter the year:"))
check400 = 0
if useryear%4==0 and useryear%400==0 or not useryear%100==0:		
	print("That is a leap year!")
else:
	print("Thats not a leap year...")
