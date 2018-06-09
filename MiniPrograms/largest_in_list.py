def biggest(Gooflat):
	if len(Gooflat) == 1:
		num = Gooflat[0]
		return num
	else:
		num = biggest(Gooflat[1:])
		if Gooflat[0] > num:
			num = Gooflat[0]
			return num
		else:
			return num
def main():
	Gooflat = [1, 2, 3,600, 6]
	print(biggest(Gooflat))

main()