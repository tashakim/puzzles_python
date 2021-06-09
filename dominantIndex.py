# Can you check if the largest element of an array is at least twice as much as every other item?
def dominantIndex(nums):
	# Naive solution
	largest = max(nums)
	for i in range(len(nums)):
		if nums[i] != largest and nums[i]*2 > largest:
			return -1
	return nums.index(largest)


def dominantIndex2(nums):
	# Shortened version
	m = max(nums)
	if all (m >= 2*x for x in nums if x != m):
		return nums.index(m)
	return -1