class DictHash():
	"""Purpose: Python dictionary implementaton of a hash table.
	"""
	def __init__(self):
		self._data = dict()

	def insert(self, key, value):
		self._data[key] = value
		print("Value : ", value, " inserted with key: ", key)
		return

	def search(self, value):
		print("Does value of: ", value, " exist in hash table?")
		for key, val in self._data.items():
			if(val == value):
				print("Yes, at key: ", key,".")
				return True
		print("No.")
		return False

	def print(self):
		print(self._data)
		return


class ListHash():
	"""Purpose: Python list implementation of a hash table.
	"""
	def __init__(self):
		self._data = []
	
	def insert(self, key, value):
		self._data.append([key,value])
		return

	def search(self, value):
		print("Does value of: ", value, "exist in hash table?")
		for item in self._data:
			if(item[1] == value):
				print("Yes, at key: ", item[0],".")
				return True
		print("No.")
		return False

	def print(self):
		print(self._data)
		return

if __name__ == "__main__":
	mylist = ListHash()
	for i in range(6):
		mylist.insert(i,i**2)

	mylist.search(16)
	mylist.search(3)

	# prints the hash table
	mylist.print()
