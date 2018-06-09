from random import randint
from movie_test import Movie


def selectionSort(values):
	for i in range(len(values)):
		minPos = minimumPosition(values,i)
		temp = values[minPos]
		values[minPos] = values[i]
		values[i] = temp

def minimumPosition (values, start):
	minPos = start
	for i in range(start +1, len(values)) :
		if values[i].getMovie() < values[minPos].getMovie():
			minPos = i

	return minPos

def minimumPosition2(values, start):
	minPos2 = start
	for i in range(start +1, len(values)) :
		if values[i].getRelease() < values[minPos2].getRelease():
			minPos2 = i
	return minPos2

def main():

	movie1 = Movie('Godzilla', 2010, 'Hollywood')
	movie2 = Movie("Return of the GhufLat", 2016,'Hollywood')
	movie3 = Movie("Chocolate Factory", 2013, "Disney")
	movie4 = Movie("Wall-e", 2015,'Pixar')
	movie5 = Movie("Cars", 2011, "Pixar")
	movielist = [movie1,movie2,movie3,movie4,movie5]
	selectionSort(movielist)
	for i in movielist:
		print(i)
main()

