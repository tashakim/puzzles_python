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


if __name__ == "__main__":
	r = Recursion()
	assert(r.power(2, 6) == 64), "Wrong value"
	assert(r.fibonacci(5) == 5), "Wrong value"
	assert(r.fibonacci(6) == 8), "Wrong value"

	print("Tests passed!")