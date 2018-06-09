from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')

def hello_world():

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += '<form method ="POST"action="form_input">\n'
	html += 'Enter temp in F: <input type ="text" name ="fahr"/>'
	html += '<input type="submit" value = "submit"/>\n'
	html += '</body>\n'
	html += '</html>\n'
	return html

@app.route('/form_input', methods = ['POST'])
def form_input():
	fahrenheit = request.form['fahr']
	fahrenheit = float(fahrenheit)

	Celsius = (fahrenheit - 32) * 5/9
	Celsius = str(Celsius)

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += 'The temp in Celsius is'+ Celsius + "!\n"
	html += '</body>'
	html += '</html>'
if __name__ =='__main__':
	app.run()
