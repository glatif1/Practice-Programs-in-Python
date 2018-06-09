
file = open("inputfile.txt",'r')
lines = file.readlines()

i = 0

file1 = open('outputfile.txt', 'w')
while i != len(lines):
	print(lines[i])
	file1.write(lines[i])
	i+=1
