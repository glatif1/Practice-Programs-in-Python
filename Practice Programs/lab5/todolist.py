from flask import Flask
from flask import request
newlist = []
completedlist=[]
app = Flask(__name__)


@app.route('/')

def hello_world():

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += '<form method = "POST" action = "form_input">'
	html += 'Enter a To-Do Item: <input type ="text" name ="item"/>\n'

	html += '<input type = "submit" value="Add item"/>'
	html += '</body>\n'
	html += '</html>\n'
	return html


@app.route('/addmore', methods = ['POST'])
def addmore():

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += '<form method = "POST" action = "form_input">'
	html += 'Enter another Item: <input type ="text" name ="item"/>\n'
	html += '<input type = "submit" value="Add"/>'
	html += '</body>\n'
	html += '</html>\n'
	return html


@app.route('/form_input', methods = ['POST'])

def form_input():
	item = request.form['item']
	newlist.append(item)
	html = ""
	html += '<html>\n'
	html += '<body>\n'

	html += "<label>To-Do List:</label></br>"
	for word in newlist:
		html += '<input type ="checkbox" name="check"/>\n'
		html += word
		html += "</br>\n"

	
	

	html += '<form method = "POST" action = "addmore">'
	html += '<input type = "submit" value="Add More"/></br>'

	# html += '<form method = "POST" action ="completed">'
	# html += '<input type = "submit" value="Complete"/>'
	html += '</body>\n'
	html += '</html>\n'

	return html

@app.route('/completed', methods = ['POST'])



def completed():
	val = request.form.getlist('check')
	for word in val:
		 print(request.form.get(word))
	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += '<form method = "POST" action = "addmore">'
	html += '<ul>'

	for word in newlist:
		
		print(word, val)
		if val:
			print(val)
			completedlist.append(word)
	for word in completedlist:
		html +="<li>"
		html += word
		html += "</li>"
	html += '<ul>'
	html += '<input type = "submit" value="Add More"/>'
	html += '</body>\n'
	html += '</html>\n'
	return html


if __name__ =='__main__':
	app.run()

