class InvalidInputException(ValueError):
	pass


def binaryInc(number):
	if number == []:
		number.append(1)
		return 
	# 0 + 1 -> 1
	if number.pop() == 0:
		number.append(1) 
	# 1 +1 -> 10
	else: 
		binaryInc(number)
		number.append(0)
	return number


if __name__ == "__main__":
	print(binaryInc([1,0,0]))
	print(binaryInc([1,1]))