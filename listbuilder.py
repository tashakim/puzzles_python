def listbuilder(n):
	"""Purpose: Builds the full list in memory.
	"""
	num, nums_list = 0, []
	while(num < n):
		nums_list.append(num)
		num +=1
	return nums_list

sum_to_n = sum(listbuilder(1000))
print(sum_to_n)

class better_builder(object):
	"""Purpose: Improves space complexity of listbuilder.
	Disadvantage: There is a lot of boilerplate. Logic is 
	convoluted.
	"""
	def __init__(self, n):
		self._n = n
		self._num = 0

	def __iter__(self):
		return self

	def __next__(self):
		return self.next()

	def next(self):
		if(self._num < self._n):
			cur, self._num = self._num, self._num + 1
			return cur
		else:
			raise StopIteration()


sum_to_n = sum(better_builder(1000))
print(sum_to_n)

