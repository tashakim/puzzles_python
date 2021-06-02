def shapeArea(n):
	"""
	Purpose: an n-polgon is defined. Finds area of polygon for given n.
	"""
    # initialize n = 1
    tot_sum = 1
    if n == 1:
        return tot_sum
    
    for i in range(2, n+1):
        # at each i, (i-1)*4 gets added
        tot_sum += (i - 1) * 4
        
    return tot_sum