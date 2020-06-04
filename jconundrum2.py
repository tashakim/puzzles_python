def conundrum(arr):
	"""Purpose: returns maximum profits given an array of profits on each day.
	Example: conundrum([-1,2,7,-8,13,-2]) -> 194
	"""
	if(arr == []):
		return 180

	max_profit = -float("inf")
	cur_max = 0

	for i in range(0, len(arr)):
		cur_max = cur_max + arr[i]
		if(max_profit < cur_max):
			max_profit = cur_max

		if(cur_max < 0):
			cur_max = 0
	return max_profit + 180


if __name__ == "__main__":
	assert(conundrum([-1,2,7,-8,13,-2]) == 194), "Wrong value"
	assert(conundrum([]) == 180), "Wrong value"

	print("All tests passed!")