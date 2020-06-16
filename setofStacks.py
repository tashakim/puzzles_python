class EmptyStackException(Exception):
	pass

class SetOfStacks:
	def __init__(self, cap):
		self._data = [None]*cap
		self._capacity = cap
		self._size = 0
		return

	def pop(self):

		if(self._data == [] or self._data == None):
			raise EmptyStackException("Stack is empty.")
		self._data.pop(-1)
		self._size -=1
		return

	def push(self, item):
		if(self._size < self._capacity):
			self._data.append(item)
			self._size +=1
		else:
			# create new stack.
			for i in range(self._capacity):
				self._data.append(None)
			self._capacity *=2
			self._size +=1
		
		return

	def printStack(self):
		print(self._data)
		return

	def popAt(self, n):
	 	# needs work
		return


if __name__ == "__main__":
	s = SetOfStack(5)
	for i in range(4):
		s.push(1)
	s.printStack()
	s.push(1)
	s.printStack()

	s.push(1)
	s.printStack()