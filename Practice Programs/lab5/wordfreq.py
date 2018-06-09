from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')

def hello_world():

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += '<form method ="POST"action="no_nothing">\n'
	html += 'Type up a string: <input type ="text" name ="string"/>'
	html += '<input type="submit" value = "submit"/>\n'
	html += '</body>\n'
	html += '</html>\n'
	return html

@app.route('/no_nothing', methods = ['POST'])
def no_nothing():
	string = request.form['string']
	string = string.split()
	worddict ={}
	for oneword in string:
		oneword = oneword.strip("'.,?!")
		oneword = oneword.strip('"')
		oneword = oneword.strip('-:;')
		if oneword in worddict:
			worddict[oneword] += 1
		else:
			worddict[oneword] = 1
		

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += "<table border =.5>"
	html += "<tr>\n"
	html += "<th>Word</th>\n"
	html += "<th> Frequency</th>"
	html += "</tr>"
	for word in worddict:
		html += "<tr>"
		html += "<td>"
		html += word
		html += "</td>"
		html += "<td>"
		html += str(worddict[word])
		html += "</td>"
		html += "</tr>"

	html += '</body>'
	html += '</html>'
	return html 


if __name__ =='__main__':
	app.run()
