class InvalidKeyException(Exception):
	"""Exception is raised when key does not exist
	in the hashtable.
	"""
	pass

class HashTable:
	"""Simple python implementation of a hash table.
	"""
	def __init__(self, n = 5)
		self._table = [[] for x in range(n)]
		self._hashtable_size = n

	def __getitem__(self, key):

	def __len__(self):
		return #sum(len(sublist) for sublist in self._table)

	def hash(self, key):
		"""Purpose: Returns the index of the table, 
		for a specific string 'key'.
		"""
		return hash(key) % self._length

	def get_value(self, key):
		"""Purpose: Returns the value associated with
		'key' in the hash table.
		"""
		if(self[key] is not None):
			return self[key]
		else:
			raise InvalidKeyException("Key is invalid.")

	def insert(self, key, value):
		"""Purpose: Appends a value to the hash table,
		by its key.
		"""
		return 

	def find(self, key):
		"""Purpose: Gets a value in hash table by key.
		"""
		return

	def delete(self, key):
		"""Purpose: Removes a value from the hash table.
		"""
		return

