def recursive_print(n):
	if n == 1:
		print(n)
	else:
		recursive_print(n-1)
		print(n)


def main():
	recursive_print(7)

main()