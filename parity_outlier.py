class InvalidInputException():
	pass

def find_outlier(arr):
	"""Purpose: Given an array either entirely
	comprised of odd or even integers except for 
	a single integer N, returns this 'outlier'.
	"""
	d = {}
	v = [None]*len(arr)
	for i in range(len(arr)):
		if(not isinstance(arr[i], int)):
			raise InvalidInputException("Input arrray is invalid.")
		d[arr[i]] = arr[i]%2
		v[i] = arr[i]%2

	if(sum(v) > 1):
		# returns the key with value 0
		return list(d.keys())[list(d.values()).index(0)]
	else:
		# returns the key with value 1
		return list(d.keys())[list(d.values()).index(1)]


def better_sol(arr):
	odd = [x for x in arr if x%2 ==1] # list of odds
	even = [x for x in arr if x%2 ==0] # list of evens

	return odd[0] if len(odd) ==1 else even[0]


def test():
	a = [2, 4, 0, 100, 4, 11, 2602, 36]
	assert(find_outlier(a) == 11), "Wrong answer." 
	assert(find_outlier(a) == better_sol(a))

	a2 = [160, 3, 1719, 19, 11, 13, -21]
	assert(find_outlier(a2) == 160), "Wrong answer."
	assert(find_outlier(a2) == better_sol(a2))

	a3 = [8485485, 3729029, 3635029, 5884963, -7797431, -4236583, 684243, -8529067, -1511933, -4441725, -9430727, 1781227, -9654751, 1634551, 7988129, 9904101, -7784043, 3900090, -4429841, -5604833, 906063, -4519939, 1487665, -1007631, 3123563, 2043561, -4607647, 6846603, 5987767, -8299321, -5093359, 4508275, 5460965, -7179645, 890367, 4395679]
	assert(find_outlier(a3) == 3900090), "Wrong answer."
	assert(find_outlier(a3) == better_sol(a3))


if __name__ == "__main__":
	test()
	print("All tests passed!")
