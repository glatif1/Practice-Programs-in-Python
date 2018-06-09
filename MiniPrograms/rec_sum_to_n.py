def recsumton(n):
	if n == 1:
		return n
	else:
		return recsumton(n-1)+(n)

def main():
	print(recsumton(6))
main()