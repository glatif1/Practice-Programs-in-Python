import os 

file = open("inputfile.txt",'r')
lines = file.readlines()

i = len(lines)-1

file1 = open('outputfile.txt', 'w')
while i != -1:
	print(lines[i])
	file1.write(lines[i])
	i-=1
