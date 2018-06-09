
def mult(n,j):
	if n == 0:
		return n
	else:
		ans = mult(n-1,j)
		return ans + j


def main():
	ans2 = mult(8,0)
	print(ans2)
main()
