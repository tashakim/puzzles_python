class Recursion:
	def power(self, num, pwr):
		"""Purpose: 
		"""

		# Breaking condition
		if pwr == 0:
			return 1

		return self.power(num, pwr-1) * num


	def fibonacci(self, num):
		"""Purpose:
		"""

		# Breaking condition
		if num == 0:
			return 0

		elif num == 1:
			return 1

		return self.fibonacci(num-1) + self.fibonacci(num-2)


	def factorial(self, num):
		"""Purpose:
		"""

		# Breaking condition

		return


	def findItem(self, data, item):
		"""Purpose:
		"""

		# Breaking condition
		if len(data) == 1:
			return data.pop() == item

		if item == data[-1]:
			return True

		return self.findItem(data[:-1], item)

### Cool!
	def findMax(self, data):
		"""Purpose: Computes maximum value in input array recursively.
		Time complexity: O(n)
		"""

		# Breaking condition
		if len(data) == 1:
			return data.pop()

		op1 = data[0]
		op2 = self.findMax(data[1:])
		
		if op1 > op2:
			return op1
		else:
			return op2


if __name__ == "__main__":
	r = Recursion()
	assert(r.power(2, 6) == 64), "Wrong value"
	assert(r.fibonacci(5) == 5), "Wrong value"
	assert(r.fibonacci(6) == 8), "Wrong value"
	assert(r.findItem([1,2,3,4], 5) == False), "Wrong value"
	r.findMax([1,2,3,4,6,4,2,9,1,3,8])

	print("Tests passed!")