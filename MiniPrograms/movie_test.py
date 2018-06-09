class Movie:
	def __init__(self, movietitle, release, studio):
		self._movietitle = movietitle
		self._release = release
		self._studio = studio

	def getMovie(self):
		return self._movietitle
	def setMovie(self, newtitle):
		self._movietitle = newtitle


	def getRelease(self):
		return self._release
	def setRelease(self, newRelease):
		self._release = newRelease


	def getStudio(self):
		return self._studio
	def setStudio(self, newStudio):
		self._studio = newStudio


	def __str__(self):
		return "Title: " + self._movietitle + " Release:" + str(self._release) + " Studio:" + self._studio
