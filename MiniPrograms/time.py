userseconds=int(input("Enter the number of seconds:"))

days = hours = minutes = 0

if userseconds>=86400:
	days=userseconds//86400
	userseconds=userseconds%86400
if userseconds >= 3600:
	hours=userseconds//3600
	userseconds=userseconds%3600
if userseconds >= 60:

	minutes=userseconds//60
	userseconds=userseconds%60



"""if userseconds>=3600:
	hours = userseconds // 3600
	userseconds = userseconds %3600"""

print("Days:", days,"Hours:" , hours, "Minutes:", minutes,"Seconds:",userseconds)

"""if userseconds >=3600 and userseconds <86400:
	hours=userseconds//3600
	hours1=userseconds%3600
	remaingingminutes=hours1//60
	remaingingminutes1=hours%60
	remainingseconds=remaingingminutes1%3600
	print(remainingseconds, remaingingminutes, hours)"""

