import random

class ShuffleArr:
	"""
	Randomly shuffles an integer array `nums`.
	"""
	def __init__(self, nums):
		self.arr = nums
		self.original = nums.copy()
		self.length = len(nums)
	
	def reset(self):
		self.arr = self.original
		self.original = self.original.copy()
		return self.arr
		
	def shuffle(self):
		for i in range(self.length):
			k = random.randrange(i, self.length)
			self.arr[i], self.arr[k] = self.arr[k], self.arr[i]
		return self.arr

# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()