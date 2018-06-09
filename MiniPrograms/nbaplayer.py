class NBAplayer:
	def __init__(self, name, team, age):
		self._name= name
		self._team = team
		self._age = age

	def getName(self):
		return self._name
	def setName(self, newname):
		self._name= newname

	def getTeam(self):
		return self._team
	def setTeam(self, newTeam):
		self._team = newTeam

	def getAge(self):
		return self._age
	def setAge(self, newage):
		self._age= newage

	def __str__(self):
		Alarkstring= "Name:"+ self._name+'\n' + "Team:" + self._team +'\n' + "Age:" + str(self._age)
		return Alarkstring
