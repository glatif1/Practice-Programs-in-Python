baseinterest = 3.5
a = input("Are your single or married:")
maritalstatus = a.lower()
age = int(input("Enter your age: "))
creditscore = int(input("Enter credit score: "))


if age < 25:
	baseinterest=baseinterest+1.5
if age >= 50:
	baseinterest=baseinterest-.5
if maritalstatus == "married":
	baseinterest=baseinterest-.75
if creditscore <550:
	baseinterest=baseinterest+2.5
if creditscore >=550 and creditscore <=650:
	baseinterest = baseinterest +1.5
if creditscore >650:
	baseinterest = baseinterest -.5
print("Your interest rate is",baseinterest,"%")