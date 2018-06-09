


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
file.write("</table")
file.write("</body>")
file.write("</html>")

print("Done writing file!")
file.close()
