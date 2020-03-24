def countbin(n) :
	return list(bin(n)).count('1')


if __name__ == "__main__" :
	print(countbin(3))