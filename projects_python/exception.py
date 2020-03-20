class InvalidInputException(Exception):
	pass

def exception(n) :
	if n<=0:
		raise InvalidInputException("Input must be greater than or equal to 0")

if __name__ == "__main__":
	print("Input a positive number: \n")
	exception(3)
	#exception(0) this guy raises the exception