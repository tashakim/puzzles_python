def rotateImage(a):
	# Purpose: rotates array in-place
	a.reverse()

	for i in range(len(a)):
		for j in range(i):
			a[i][j], a[j][i] = a[j][i], a[i][j]

	return a


def rotateImage1(a):
	# Purpose: rotates array, with O(n*n) space complexity
    # [[1,2,3], [4,5,6], [7,8,9]]
    # [[7,4,1], [8,5,2], [9,6,3]]
    # take the subarr[0] from arr[-1:0:-1]
    # then take subarr[1] from arr[-1:0:-1]
    # then take subarr[2] from arr[-1:0:-1]
    n = len(a) 
    res = [[None for i in range(n)] for i in range(n)]
    """
    a[0][0] = a[n][0]
    a[0][1] = a[n-1][0]
    a[0][2] = a[n-2][0]
    
    a[1][0] = a[n][1]
    a[1][1] = a[n-1][1]
    a[1][2] = a[n-2][1]
    """
    for i in range(n):
        for j in range(n):
            res[i][j] = a[n-1-j][i]
            
            #print(a[i][j], i, j, "dd", cpy[n-1-j][i], n-1-j, i)
            #a[0][0] = cpy[2][0]
            #a[0][1] = cpy[1][0]
            #a[0][2] = cpy[0][0]
        
    return res