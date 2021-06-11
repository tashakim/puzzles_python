# Classic problem, can you implement a min-stack supporting O(1) operations?
# That is, implement the methods push, pop, peek, as well as getMin.

class MinStack:
	def __init__(self):
		self.min = [float('inf')] # acts as a snapshot
		self.data = []

	def push(self, x):
		self.data.append(x)
		if x < self.min[-1]:
			self.min.append(x)
		else: self.min.append(self.min[-1])

	def pop(self):
		self.data.pop()
		self.min.pop()

	def peek(self):
		return self.data[-1]

	def getMin(self):
		return self.min[-1]
