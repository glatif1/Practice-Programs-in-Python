from random import randint
class Choices:
	def __init__(self, name, choice):
		self._name = name
		self._choice = choice

	def getname(self):
		return self._name
	def setname(self, newname):
		self._name= newname


	def getchoice(self):
		return self._choice 
	def setchoice(self):
		self._choice = randint(1,3)
		
		if self._choice == 1:
			self._choice = 'Rock'
		if self._choice == 2:
			self._choice='Paper'
		if self._choice == 3:
			self._choice= 'Scissors'
		return self._choice
	def __str__(self):
		output = "hello " + self._name + ' your attack method was ' + str(self._choice)
		return output


