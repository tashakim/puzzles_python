def increasing_subseq(arr):
    """
    Purpose: Returns the no. of triplets (i, j, k) where 
    1. i < j < k
    2. arr[i] < arr[j] < arr[k]
    """
    res = [0]*len(arr)
    
    for k in range(1, 4):
        for i in range(len(arr)):
            if k == 1:
                res[i] = 1
            else:
                res[i] = 0
                for j in range(i+1, len(arr)):
                    if arr[j] > arr[i]:
                        res[i] += res[j]
    return sum(res)