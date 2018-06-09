from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')

def hello_world():

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += '<form method ="POST"action="form_input">\n'
	html += 'Enter First number: <input type ="text" name ="num1"/>'
	html += 'Enter Second number: <input type ="text" name ="num2"/>'
	html += 'Enter operation: <input type ="text" name ="operate"/>'
	html += '<input type="submit" value = "submit"/>\n'
	html += '</body>\n'
	html += '</html>\n'
	return html

@app.route('/form_input', methods = ['POST'])
def form_input():
	number1 = request.form['num1']
	number2 = request.form['num2']
	operation = request.form['operate']


	number1 = float(number1)
	number2 = float(number2)
	answer = 0 

	print(number1, number2)

	operation = operation.rstrip() 

	if operation == "+":
		answer = number1 + number2
	if operation == "*":
		answer = number1 * number2
	if operation == '-':
		answer = number1 - number2
	if operation == "/":
		answer = number1/number2
		

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += 'The answer is '+ str(answer) + "!\n"
	html += '</body>'
	html += '</html>'
	return html 


if __name__ =='__main__':
	app.run()
