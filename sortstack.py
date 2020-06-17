class EmptyStackException(Exception):
	pass

class SortStack:
	"""Purpose: Sorts a stack such that the smallest items
	are on the top.
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

		return

	def pop(self):
		if(self._size == 0):
			raise EmptyStackException("Check again. Stack is empty.")
		else: 
			self._data.pop(self._top)
			self._size -=1
			self._top -=1
		return

	def peek(self):
		return self._data[self._top]

	def isEmpty(self):
		if(self._size == 0):
			return True
		return False


	def printStack(self):
		return

if __name__ == "__main__":
	s= SortStack()