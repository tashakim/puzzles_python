class InvalidIndeException(Exception):
	pass

class EmptyArrayException(Exception):
	pass

class DynamicArray():
	"""Purpose: dynamic array class (sim. to python list)
	"""
	def __init__ (self, cap = 1):
		self._size = 0
		self._capacity = cap
		self._array = [None]*cap

	def __repr__(self):
		return "<array object returned>"

	def __len__(self):
		"""Purpose: Returns the number of elements in the array.
		"""
		return self._size

	def __getitem__(self, k):
		"""Purpose: Returns the item at index k.
		"""
		if(k < 0 or k >= self._capacity):
			raise InvalidIndexException("Index is out of range.")
		return self._array[k]

	def append(self, item):
		"""Purpose: Adds element to end of array.
		"""
		if(self._size  <= self._capacity):
			self.resize(2*self._capacity)
		self._array[self._size] = item
		self._size += 1 

	def insertAt(self, item, index):
		"""Purpose: Inserts item at a specific index.
		"""
		if(self._size <= self._capacity):
			self.resize(2*self._cacpacity)
		for i in range(self._size -1, index -1, -1):
			self._array[i+1] = self._array[i]
		self._array[index] = item
		self._size += 1


	def remove(self):
		"""Purpose: Deletes item from end of array.
		"""
		if(self._size == 0):
			raise EmptyArrayException("Array is empty; Cannot remove from array.")
		self._array[self._size-1] = None
		# OR self._array.pop(self._size -1)
		self._size -= 1


	def removeAt(self, index):
		"""Purpose: Deletes item from a specific index.
		"""
		if(self._size == 0):
			raise EmptyArrayException("Array is empty; Cannot remove from array.")
		self._array[index] = None
		if(index == self._size -1):
			self._array[index] = None
			self._size -=1
			return

		for i in range(index+1, self._size):
			self._array[i-1] = self._array[i]
		self._size -= 1


	def resize(self, new_cap):
		"""Purpose: Resizes array to new capacity new_cap.
		"""
		newarr = [None]*new_cap
		for i in range(self._size):
			newarr[i] = self._array[i]
		self._array = newarr
		self._capacity  = new_cap
		return


if __name__ == "__main__":
	a = DynamicArray()
	a.append(1)
	print(len(a))
	a.append(2)
	print(len(a), "\n")

	print(a[0])
	print(a[1])

	# print(a)