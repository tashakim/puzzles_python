arr = [1,2,3]

# non-tail recursion
def function(arr):
	if len(arr) == 0:
		return 0
	
	return arr[0] + function(arr[1:])

# tail recursion
def tail_recurse(arr):
	def helper(arr, res):
		if len(arr) == 0:
			return res
		return helper(arr[1:], arr[0] + res)
		
	return helper(arr, 0)

class Sol:
	def version2(self, arr):
		self.res = 0
		def helper(arr):
			if len(arr) == 0:
				return self.res
			self.res += arr[0]
			return helper(arr[1:])
		
		helper(arr)
		return self.res
	
if __name__ == "__main__":
	print("Sum is: ", function(arr))
	print("Same sum?: ", tail_recurse(arr))
	s = Sol()
	print("Verion 2:" , s.version2(arr))