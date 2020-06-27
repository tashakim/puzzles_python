class ArrayStack:
	"""Purpose: Simply python implementation of 
	an array-based stack.
	"""
	def __init__(self):
		self.data = []

	def push(self, item):
		return self.data.append(item)

	def pop(self):
		return self.data.pop()

	def peek(self):
		return self.data[-1]

	def isEmpty(self):
		return self.size() == 0

	def size(self):
		return len(self.data)


def checkParantheses(s):
	"""Purpose: checks that the input string 
	has correct parenthesis expressions.
	"""
	match = {')':'(', ']':'[', '}':'{'}
	S = ArrayStack()
	for c in s:
		if (c in '([{'):
			S.push(c)
		elif(c in match):
			if(S.isEmpty()):
				return False
			else:
				if(S.pop() != match[c]):
					return False
	return True

if __name__ == "__main__":
	assert(checkParantheses("(a+b)") == True), "Wrong answer"
	assert(checkParantheses("([)") == False), "Wrong answer"
	assert(checkParantheses("{)") == False), "Wrong answer"

	print("All tests passed!")
