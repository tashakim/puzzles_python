def find_outlier(arr):
	"""Purpose: Given an array either entirely
	comprised of odd or even integers except for 
	a single integer N, returns this 'outlier'.
	"""
    d = {}
    v = [None]*len(arr)
    
    for i in range(len(arr)):
        d[arr[i]] = arr[i]%2
        v[i] = arr[i]%2
        
    if(sum(v) > 1):
    	# returns the key with value 0
        return list(d.keys())[list(d.values()).index(0)]
    	
    else:
    	# returns the key with value 1
        return list(d.keys())[list(d.values()).index(1)]


if __name__ == "__main__":
	a = [2, 4, 0, 100, 4, 11, 2602, 36]
	assert(find_outlier(a) == 11), "Wrong answer." 

	a2 = [160, 3, 1719, 19, 11, 13, -21]
	assert(find_outlier(a2) == 160), "Wrong answer."

	a3 = [8485485, 3729029, 3635029, 5884963, -7797431, -4236583, 684243, -8529067, -1511933, -4441725, -9430727, 1781227, -9654751, 1634551, 7988129, 9904101, -7784043, 3900090, -4429841, -5604833, 906063, -4519939, 1487665, -1007631, 3123563, 2043561, -4607647, 6846603, 5987767, -8299321, -5093359, 4508275, 5460965, -7179645, 890367, 4395679]
	assert(find_outlier(a3) == 3900090), "Wrong answer."
	
	print("All tests passed!")
