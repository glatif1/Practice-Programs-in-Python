import tmdbsimple as tmdb
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
	html += 'Enter Movie Name: <input type ="text" name ="movie"/>'
	html += '<input type="submit" value = "submit"/>\n'
	html += '</body>\n'
	html += '</html>\n'
	return html

@app.route('/form_input', methods = ['POST'])
def form_input():
	movie1 = request.form['movie']
	tmdb.API_KEY = '20c8defe43f8d8dfede86e30ade4f929'
	movie = tmdb.Search()
	response = movie.movie(query=movie1)
	html = " "
	html += '<html>\n'
	html += '<body>\n'
	html += '<table border =1 >'

	html+='<th>'
	html+= 'Title'
	html += '</th>'
	html += '<th>'
	html += 'ID'
	html += '</th>'
	html += '<th>'
	html += 'Release Date'
	html+= '</th>'
	html += '<th>'
	html += 'Populatirty'
	html += '</th>'
	for s in movie.results:

		title = s["title"]
		ID = s['id']
		release_date = s['release_date']
		popularity = s['popularity']
		html += '<tr>'
		html +='<td>'
		html += title
		html += '</td>'
		html += '<td>'
		html += str(ID)
		html +='</td>'
		html += '<td>'
		html += str(release_date)
		html += '</td>'
		html += '<td>'
		html += str(popularity)
		html += '</td>'
		html += '</tr>'

	html += '</table>'
	html += '<a href="/">Back</a>'
	html += '</body>'
	html += '</html>'
	return html 

	
if __name__ =='__main__':
	app.run()
