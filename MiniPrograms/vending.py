dollarAmount= float(input("Enter amount of money$:"))
soda = 1.15 
amountofsoda = dollarAmount//soda
change = dollarAmount-(amountofsoda*soda)
remainingchange=change
if remainingchange >= .25:
	quarters = remainingchange//.25
	remainingchange = remainingchange%.25
	print("Quarters:", quarters)
if remainingchange >= .10:
	dimes = remainingchange//.10
	remainingchange = remainingchange%.10
	print("Dimes:",dimes)
if remainingchange >= .05:
	nickels= remainingchange//.05
	remainingchange = remainingchange%.05
	print("Nickels",nickels)
if remainingchange >=.01:
	pennies = remainingchange//.01
	remainingchange = remainingchange%.01
	print("Pennies:",pennies)


print("Change is:",change)
print ("Number of soda cans:",amountofsoda)