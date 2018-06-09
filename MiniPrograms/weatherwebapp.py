from flask import Flask
from flask import request
from pyowm import OWM

app = Flask(__name__)


@app.route('/')

def hello_world():

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += '<form method ="POST"action="form_input">\n'
	html += 'Enter Country: <input type ="text" name ="country"/>'
	html += 'Enter City: <input type ="text" name ="city"/>'
	html += '<input type="submit" value = "submit"/>\n'
	html += '</body>\n'
	html += '</html>\n'
	return html

@app.route('/form_input', methods = ['POST'])
def form_input():
	city = request.form['city']
	country = request.form['country']
	owm = OWM(API_key='c4c27280349fce4e3bb120031151146b')
	obs = owm.weather_at_place(city+","+country)
	w = obs.get_weather()
	print(w.get_temperature("fahrenheit"))

	temp_dictionary = w.get_temperature("fahrenheit")

	current_temperature = temp_dictionary['temp']

	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += 'The temperature in '+ city + "is"+ str(current_temperature)+"!\n"
	html += '</body>'
	html += '</html>'
	return html 

	
if __name__ =='__main__':
	app.run()
