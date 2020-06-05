class MySet():
	def __init__(self):
		self._size = 0
		self._set = {}
		print("New set was created.")

	def add(self, item):
		self._set.add(item)
		self._size +=1
		print(item, " was added to your set.")

	def remove(self, item):
		self._set.remove(item)
		self._size -=1
		print(item, " was removed from your set.")
		return item
	
	def contains(self, item):
		return item in self._set

	def size(self):
		return self._size 

	def isEmpty(self):
		return self._size == 0

	def enumerate(self):
		

if __name__ == "__main__":
	s = MySet()
	s.add(2)
	s.add(3)
	s.remove(2)

	print(s.contains(2))
	print(s.contains(3))
