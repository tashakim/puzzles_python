class InvalidInputException(ValueError):
	pass


def binaryInc(number):
	#converts number to list
	number = [int(i) for i in str(number)]

	binInc_helper(number)
	return number

	

def binInc_helper(number):
	if number == []:
		number.append(1)
		return 
	# 0 + 1 -> 1
	if number.pop() == 0:
		number.append(1) 
	# 1 +1 -> 10
	else: 
		binInc_helper(number)
		number.append(0)
	return number


if __name__ == "__main__":
	print(binaryInc(100))
	print(binaryInc(11))

	assert binaryInc(0) == [1], "Test failed"
	assert binaryInc(1) == [1,0], "Test failed"
	assert binaryInc(101) == [1,1,0], "Test failed"