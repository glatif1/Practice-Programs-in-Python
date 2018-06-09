from sys import argv 


myfile = open(argv[1], 'r')
stopfile = open('stopwords.txt', "r")

words = stopfile.readlines()

stopwords = [word.rstrip() for word in words] 

worddict ={}
actual ={}
for line in myfile:
	words = line.split()
	for oneword in words:
		oneword = oneword.strip("'.,?!")
		oneword = oneword.strip('"')
		oneword = oneword.strip('-:;')
		if oneword in worddict:
			worddict[oneword] += 1
		else:
			worddict[oneword] = 1
	if worddict[oneword] >= 50:
		if oneword not in stopwords:
			actual[oneword] = worddict[oneword] 




print(actual)


dictionary = actual.copy()

file = open("frequency.html", "w")

file.write("<!DOCTYPE html>")
file.write("<html>")
file.write("<body>")
file.write("Hello! Bring it!")

file.write("<table border =1>")
file.write("<tr>\n")
file.write("<th>Words</th>")
file.write("<th>Frequency</th>\n")
file.write("</tr>")

for word in dictionary:
	print(word, dictionary[word])
	file.write("<tr>")
	file.write("<td>")
	file.write(word)
	file.write("</td>")
	file.write("<td>")
	file.write(str(dictionary[word]))
	file.write("</td>")
	file.write("</tr>")
file.write("</table")
file.write("</body>")
file.write("</html>")

print("Done writing file!")
file.close()
		
