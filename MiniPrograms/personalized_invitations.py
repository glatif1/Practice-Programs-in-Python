file = open("invites.csv", "r")
lines = file.readlines()

# words =lines[1].split(",")
# print(words[0])

i=0

while i < len(lines)-1:
	i+=1
	print(i)
	filename = "invite"+str(i)+".csv"
	fileout = open(filename,'w')
	
	# file = open("invites.csv", "r")
	# line = file.readline()
	
	words = lines[i].split(",")
	fileout.write(words[0])


	# for line in file:
	# 	words = line.split(",")
	# 	fileout.write(words[0])

	fileout.close()

	
file.close()