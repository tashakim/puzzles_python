class HashTable:
	def __init__(self, n = 5)
		self._table = [None]*n
		self._length = len(self._table)

	def hash(self, key):
		"""Purpose: Returns the index of the table, 
		for a specific string 'key'.
		"""
		return hash(key) % self._length

	def append(self, key, value):
		"""Purpose: Appends a value to our table,
		by its key.
		"""
		return 

	def get(self, key):
		"""Purpose: Gets a value by the key.
		"""
		return