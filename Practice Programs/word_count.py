from sys import argv 


for i in range(1,len(argv)):
	file = argv[i]
	openedfile = open(file, 'r')
	lines = openedfile.readlines()
	for i in lines:
		print(i)
#print(lines)



# i=-1
# while i <len(openedfile):
# 	if argv[1] in lines[i]:
# 		print("found:", lines[i])
# 		i = len(lines)
# 	else:
# 		i+=1



