class SimpleMinstack:
	"""Purpose: Dynamic programming; min value is an invariant.
	"""
	def __init__(self):
		self.stack = []

	def push(self, x:int) -> None:
		if(not self.stack):
			self.stack.append((x,x))
			return
		current_min = self.stack[-1][1]
		self.stack.append((x, min(x, current_min)))

	def pop(self) -> None:
		self.stack.pop()

	def top(self) -> int:
		return self.stack[-1][0]

	def getMin(self) -> int:
		return self.stack[-1][1]


class Minstack:
	"""Purpose: Min value can be repetitive; using two stacks.
	"""
	def __init__(self):
		self.stack = []
		self.minstack = []

	def push(self, x:int) -> None:
		self.stack.append(x)
		if(not self.minstack[-1] or x <= self.minstack[-1]):
			self.minstack.append(x)

	def pop(self) -> None:
		if(self.minstack[-1] == self.stack[-1]):
			self.minstack.pop()
		self.stack.pop()

	def top(self) -> int:
		return self.stack[-1]

	def getMin(self) -> int:
		return self.minstack[-1]


class Minstack_tracker:
	"""Purpose: Improved use of two stacks, to check how many 
	times the value can be popped before minimum can be discarded.
	"""
	def __init__(self):
		self.stack = []
		self.minstack = []

	def push(self, x: int) -> None:
		self.stack.append(x)

		if(not self.minstack or x < self.minstack[-1][0]):
			self.minstack.append([x,1])
		elif(x == self.minstack[-1][0]):
			self.minstack[-1][1] += 1

	def pop(self) -> None:
		if(self.minstack[-1][0] == self.stack[-1]):
			self.minstack[-1][1] -= 1
		if(self.minstack[-1][1] == 0):
			self.minstack.pop()
		self.stack.pop()

	def top(self) -> int:
		return self.stack[-1]

	def getMin(self) -> int:
		return self.minstack[-1][0]


if __name__ == "__main__":

	s1 = SimpleMinstack()
	s2 = Minstack()
	s3 = Minstack_tracker()
