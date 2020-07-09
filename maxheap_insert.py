class MaxHeap:
	def__init__(self):
		self.data = [None]

	def insert(self, item):
		self.data.append(item)
		i = len(self.data)-1
		while(i > 1): # while index of item is NOT the root
			if(self.data[i] > self.data[i//2]):
				self.data[i], self.data[i//2] = self.data[i//2], self.data[i]
				i = i//2
			else:
				return
