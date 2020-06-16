class MinStack:
	"""Purpose: Design a stack which, in  addition to pop and push, has a function  min that returns the minimum element in O(1). (CTCIpg98_3.2)
	"""
	def __init__(self):
		self._data =  []
		self._min = float('inf')
		return


	def pop(self):
		"""Runtime: O(1).
		"""
		# raise EmptyStackException if empty
		self._data.pop(-1)
		return

	def push(self, item):
		"""Runtime: O(1).
		"""
		self._data.append(item)
		if(item < self._min):
			self._min = item
		return

	def min(self):
		"""Runtime: O(1).
		"""
		return self._min


