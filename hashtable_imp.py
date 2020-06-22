class HashTable:
	def __init__(self, n = 5)
		self._table = [None]*n

	def hash(self, key):
		"""Purpose: Returns the index of the table, 
		for a specific string 'key'.
		"""
