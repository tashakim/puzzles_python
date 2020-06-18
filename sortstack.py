class EmptyStackException(Exception):
	pass

class SortStack:
	"""Purpose: Sorts a stack such that the smallest items
	are on the top.
	Idea 1: hint: sort elements within stack.
	Idea 2 hint: use three stacks, two of which are temporary.
	"""
	def __init__(self, cap):
		self._data = [None]*cap
		self._capacity = cap
		self._size = 0
		self._top = 0
		return

	def push(self, item):
		if(self._size < self._capacity):
			self._data.append(item)
			self._size +=1
			self._top +=1
		# sorts all items after appending.
		return


	def pop(self):
		if(self._size == 0):
			raise EmptyStackException("Check again. Stack is empty.")
		else: 
			self._data.pop(self._top)
			self._size -=1
			self._top -=1
		# sorts remaining items after removing.
		return


	def peek(self):
		return self._data[self._top]

	def isEmpty(self):
		if(self._size == 0):
			return True
		return False


	def printStack(self):
		return

	def test():
		s1 = sortStack()
		for i in ragne(3):
			s1.push(i)
		return

if __name__ == "__main__":
	s= SortStack()
	test()

