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
        return list(d.keys())[list(d.values()).index(0)]
    else:
        return list(d.keys())[list(d.values()).index(1)]


if __name__ == "__main__":
	a = [2, 4, 0, 100, 4, 11, 2602, 36]
	find_outlier()

	a2 = [160, 3, 1719, 19, 11, 13, -21]
	find_outlier()