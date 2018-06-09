import sys

file1List = []

file2List = []

file1Dict = {}




file1 = sys.argv[1]
file2 = sys.argv[2]

file2Dict = {}
inFile1 = open(file1, "r")
inFile2 = open(file2, "r")
inbothfile = open("both.txt", 'w')
uniqueforfile = open("unique.txt", 'w')
infirstfile = open("first.txt", 'w')
insecondfile = open("second.txt", 'w')
ineitherfile = open("either.txt", 'w')

eitherDict = {}
bothDict = {}

line1 = inFile1.readlines()
line2 = inFile2.readlines()

for i in line1:
	word = i.lower().split()
	file1List += word

for i in line2:
	word = i.lower().split()
	file2List += word

for word in file1List:
	if word in bothDict:
		bothDict[word] += 1
	if word not in bothDict:
		bothDict[word] = 1

for word in file2List:
	if word in bothDict:
		bothDict[word] += 1
	if word not in bothDict:
		bothDict[word] = 1

for key in sorted(bothDict):
	inbothfile.write(key + "\n")

for key in sorted(bothDict):
	if bothDict[key] == 1:
		uniqueforfile.write(key + "\n")

for word in file1List:
	if word not in file1Dict:
		file1Dict[word] = 1


for word in file2List:
	if word in file1Dict:
		file1Dict[word] = file1Dict[word] - 1

	
for word in file1Dict:
	if file1Dict[word] == 1:
		infirstfile.write(word + "\n")

for word in file2List:
	if word not in file2Dict:
		file2Dict[word] = 1


for word in file1List:
	if word in file2Dict:
		file2Dict[word] = file2Dict[word] - 1


for word in file2Dict:
	if file2Dict[word] == 1:
		insecondfile.write(word + "\n")

for word in file1Dict:
	if file1Dict[word] == 1:
		eitherDict[word] = 1


for word in file2Dict:
	if file2Dict[word] == 1:
		eitherDict[word] = 1


for key in sorted(eitherDict):
	ineitherfile.write(key + "\n")


inFile1.close()
inFile2.close()
inbothfile.close()
uniqueforfile.close()
infirstfile.close()
insecondfile.close()
ineitherfile.close()