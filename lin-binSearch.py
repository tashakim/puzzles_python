def linear_search(L,x):
	count = 0
	while(count < len(L) and L[count]!=x):
		count += 1
	if(count <= len(L)):
		return count
	else:
		return -1

def binary_search(L, x):
	"""Recursive binary search implementation.
	"""
	low = 0
	high = len(L)-1
	mid = (low+high)//2

	if(high >= low):
		if(L[mid] == x):
			return mid

		elif(L[mid] > x):
			return binary_search() # saves space to not use array

""" Ignore below:

def binary_searchIter(L,x):
	low = 0
	high = len(L) -1
	
	while(high >= low):
		mid = (low+high)//2
		if(L[mid] == x):
			return mid
		elif(L[mid] > x):
			high = mid
		else

def binary_searchRec(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1

def binary_searchIter(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if x is present at mid 
        if arr[mid] < x: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif arr[mid] > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1


if __name__ == "__main__":
	l = [1,2,3,4,5,6,7,8,9,10]
	print(linear_search(l, 4))
	print(binary_search(l, 4))


