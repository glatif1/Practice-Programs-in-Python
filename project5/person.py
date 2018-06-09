class Person:
	def __init__(self, username, password, messages,friends):
		self._username= username
		self._password = password
		self._messages = messages
		self._friends = friends

	def setusersname(self, newusername):
		self._username= newusername
	def getusername(self):
		return self._username

	def setpassword(self, newpassword):
		self._password = newpassword
	def getpassword(self):
		return self._password

	def setmessages(self, newmessage):
		self._messages= newmessage
	def getmessages(self):
		return self._messages

	def setfriends(self, newfriend):
		self._friends = newfriend
	def getfriends(self):
		return self._friends

	def __str__(self):
		return "Username: "+self._username+" Password: "+self._password+" Messages: "+self._messages + " Friends: "+self._friends
