def sumint(n):
	if(n > 0):
		return n + sumint(n-1)
	else:
		return n

if __name__ == "__main__":
	a = int(input("Number: "))
	print(sumint(a))