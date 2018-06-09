def recexp(n,p):
	if p == 0:
		return 1
	else:
		return recexp(n,p-1) * n
print(recexp(3,2))