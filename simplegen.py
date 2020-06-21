def simpleGenerator():
	"""Purpose: Generates the following simple values.
	"""
	yield 1
	yield 2
	yield "last"

def listGenerator(n):
	"""Purpose: Generates positive integers up to n.
	"""
	num = 0
	for i in range(n):
		yield num
		num += 1

def infGenerator():
	"""Purpose: Generates infinite square numbers.
	"""
	num = 0
	while(True):
		yield num*num
		num += 1


if __name__ == "__main__":
	i = 0
	for item in simpleGenerator():
		print("Simple generator ", i, ": ", item)
		i += 1

	print()
	for item in listGenerator(3):
		print("list generator ", i, ": ", item)

	print()
	for item in infGenerator():
		if(item < 50):
			print(item)
		else:
			break