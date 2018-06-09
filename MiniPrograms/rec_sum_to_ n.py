def recsumton(n):
	if n == 1:
		return n
	else:
		recsumton(n-1)+recsumton(n)
print(recsumton(3))