class EmptyStackException(Exception):
	pass

class MyStack:
	def __init__(self):
		self._data = []


	def push(self, item):
		self._data.append(item)
		print(item, " was added to stack.")

		return item


	def pop(self):
		if(self._data is None):
			raise EmptyStackException("There is nothing to pop.")

		self._data.pop(-1)
		print("Item was popped from top of stack.")

		return

	def printStack(self):
		if(self._data is []):
			print("Stack is empty.")

		print("Stack contains: ", self._data)
		return


if __name__ == "__main__":
	s = MyStack()
	s.printStack()

	s.push(1)
	s.printStack()
	s.pop()
	s.printStack()
	
