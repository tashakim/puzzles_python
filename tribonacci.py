# Space vs Time complexity in Dynamic Programming:

def tribonacci(n):
	"""Purpose: Calculates the n-th tribonacci 
	number using Dynamic Programming.
	"""
	if n == 0:
		return 0
	if n == 1 or n == 2:
		return 1

	x,y,z = 0,1,1
	for i in range(n-2): 
		x,y,z = y,z, x+y+z # Optimizes space complexity
	return z


def better_tribonacci(n):
	"""Purpose: Improved solution using Dynamic Programming.
	This solution assumes that n <= 38, as problem specifies.
	We precompute Tribonacci numbers and store them in an array.
	"""
	
	nums = [0]*38 # Optimizes time complexity
	nums[1] = nums[2] = 1
	for i in range(3, 38):
		nums[i] = nums[i-1] + nums[i-2] + nums[i-3]

	return nums[n]

if __name__ == "__main__":
	assert(tribonacci(0) == 0)
	assert(tribonacci(3) == 2)
	assert(tribonacci(4) == 4)

	assert(better_tribonacci(0) == 0)
	assert(better_tribonacci(3) == 2)
	assert(better_tribonacci(4) == 4)
	print("All tests passed!")