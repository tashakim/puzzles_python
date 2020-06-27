class ArrayStack:
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
	print(checkParantheses("(a+b)"))
	print(checkParantheses("([)"))
	print(checkParanthese("{)"))