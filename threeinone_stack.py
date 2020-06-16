class EmptyStackException(Exception):
	pass

class InvlidInputException(Exception):
	pass

class Threeinone_stack():
	"""Purpose: We can use a single array to implement three (3) stacks.
	(CTCIpg98)
	"""
	def __init__(self, l):
		self._data = [None]*l # three-in-one stack
		self._mid = l//2
		self._capacity = l

		self._top1 = -1
		self._top2 = self._mid
		self._top3 = 0

		print("Three-way stack created!")
		return


	def push(self, n, item):
		"""Purpose: Pushes item to stack No. n
		"""
		if(not isinstance(item, int)):
			raise InvlidInputException("Input is invalid.")

		if(n == 1):
			self._data.insert(0,item)
			self._top1 +=1
		elif(n == 2):
			self._data.insert(self._mid, item)
			self._top2 +=1
		elif(n == 3):
			self._data.insert(-1, item)
			self._top3 -=1
		print(item, " was successfully appended to stack!")
		return


	def pop(self, n):
		"""Purpose: Pops item off the top of stack No. n
		"""
		if(self._data == [] or self._data is None):
			raise EmptyStackException("Stack  is  currently empty.")
		if(n == 1):
			item = self._data.pop(self._top1)
			self._top1 -=1
		elif(n == 2):
			item = self._data.pop(self._top2)
			self._top2 -=1
		elif(n == 3):
			item = self._data.pop(self._top3)
			self._top3 +=1
		print(item, " was successfully popped from stack No. ", n)
		return item


	def printItems(self):
		"""Purpose: Prints elements of the three-way stack.
		"""
		if(self._data == [] or self._data is None):
			raise EmptyStackException("Stack is currently empty.")
		print("Stack: ", self._data, "\n")
		return

def testStack():
	test_stack  = Threeinone_stack(3)
	test_stack.push(1,1)
	test_stack.printItems()
	test_stack.pop(1)
	test_stack.printItems()

if __name__ == "__main__":
	t = Threeinone_stack(10)
	t.push(1, 1)
	t.printItems()
			
	t.push(2, 2)
	t.push(3, 3)
	t.printItems()
			
	t.pop(1)
	t.printItems()
	#testStack()