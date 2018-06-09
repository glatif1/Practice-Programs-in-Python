low = int(input("Enter low number:"))
h = int(input("Enter high number:")) 

high = h+1 # this adds 1 to the high beause range doesn't include the last number


result=0
if low <= high:
	for i in range(low, high):
		result = result + i
		
	print(result)
else: 
	print("Error:", h ,"<" , low)