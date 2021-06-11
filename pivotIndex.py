# Find the index of the array where elements on the left have the same sum as elements on the right.
def pivotIndex(nums):
	# Loop through all indices of array
	for i in range(len(nums)):
		if sum(nums[:i]) == sum(nums[i+1:]):
			return i
	return -1

def pivotIndex2(nums):
	# Faster version, we can keep track of sum on left, with which we calculate right sum.
	# This way, we don't have O(n*n) time complexity.
	totsum = sum(nums)
	left_sum = 0

	if sum(nums[1:] == 0): return 0 # edge case: nothing on the left!

	for i in range(1, len(nums)):
		left_sum += nums[i-1]
		right_sum = totsum - left_sum - nums[i]
		if left_sum == right_sum:
			return i
	return -1