# Can you check if an array can become non-decreasing by modifying at most one element?
def editNonDecreasing(arr: List[int]) -> bool:
	# Iteratively keeps track with a global boolean.
	bool = False
	def check(arr, bool):
		for i in range(len(arr) - 1):
			if arr[i] > arr[i+1]:
				if bool == False:
					bool = True
					temp = arr.copy()
					temp.pop(i)
					arr.pop(i+1)
					return check(temp, arr) or check(arr, temp)
				else: return False
			return True
	return check(arr, bool)


def editNonDecreasing2(arr: List[int]) -> bool:
	# Try another way
    bad_idx = -1
    n = len(nums)
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            if bad_idx != -1: 
                return False
            bad_idx = i
    return bad_idx in [-1, 0, n-2] or nums[bad_idx-1] <= nums[bad_idx+1] or nums[bad_idx] <= nums[bad_idx+2]