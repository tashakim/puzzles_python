# How many reduction operations do we need to make all items in an array equal? 
def reductionOperations(nums):
	res, count = 0, 0
	nums.sort()
	for i in range(len(nums)):
		if nums[i] > nums[i-1]:
			count += 1
		res += count
	return res

# Step 1
# [1,1,2,2,3]

# Step 2
# [1,1,2,2,2]

# Step 3
# [1,1,1,2,2]

# Step 4
# [1,1,1,1,2]

# Step 5
# [1,1,1,1,1]
