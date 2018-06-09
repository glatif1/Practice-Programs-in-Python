original =num = int(input("Enter number:"))
result=1
if num ==0:
	print(1)
else:
	while num > 0:
		result = result * num
		num = num -1
	print(original,"!=",result)