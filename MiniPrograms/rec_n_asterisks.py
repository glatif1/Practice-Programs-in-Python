def stars(n):
	if n == 0:
		return n
	else:
		stars(n-1)
		print("*"*n)
		
def main():
	stars(8)

main()