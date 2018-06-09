
def recsum(list1):
	if len(list1) ==1 :
		return list1[0]
	else:
		return recsum(list1[1:])+list1[0]
list1 = [1,1,1,7,1,1,7]
print(recsum(list1))