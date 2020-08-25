class Solution:
	def xorOperation(self, n: int, start: int) -> int:
		"""Purpose: Returns the bitwise XOR of all elements shifted
		by an increasing power of 2.
		"""
		res = 0
		for i in range(n):
			res ^= start + 2*i
		return res 

	def xorOperation2(self, n, start):
		return [0^start+2*i for i in range(n)][-1]



if __name__ == "__main__":
	s = Solution()
	assert(s.xorOperation(n=5, start = 0) == 8), "Wrong output"
	assert(s.xorOperation2(n=5, start = 0) == 8), "Wrong output"
	
	assert(s.xorOperation(n=4, start = 3) == 8), "Wrong output"
	assert(s.xorOperation2(n=4, start = 3) == 8), "Wrong output"

	print("All tests passed!")