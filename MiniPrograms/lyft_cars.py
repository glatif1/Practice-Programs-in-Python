number_of_passengers = int(input("Enter the number of passengers:"))

resultofdiv = number_of_passengers//4

modulus_answer = number_of_passengers%4

if modulus_answer > 0:
	resultofdiv+=1
else:
	print(resultofdiv)

print("the numer of cars is:", resultofdiv)