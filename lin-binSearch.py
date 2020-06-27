def linear_search(L,x):
	count = 0
	while(count < len(L) and L[count]!=x):
		count += 1
	if(count <= len(L)):
		return count
	else:
		return -1

def binary_search(arr, x): 
	low = 0
	high = len(arr)-1
	print("binary search called on: \n", arr)
	print("low = ", low, ", high = ", high, "\n")

	if(high >= low):
		mid = (high+low)//2
		if(arr[mid] == x):
			print("x found\n")
			print("mid = ", mid)
			return mid
		elif(arr[mid] > x):
			return binary_search(arr[:mid], x)
		else:
			return binary_search(arr[mid+1:], x)
	else:
		return -1


def binary_searchRec(arr, low, high, x): 
	if(high >= low):
		mid = (high+low)//2
		if(arr[mid] == x):
			return mid
		elif(arr[mid] > x):
			return binary_searchRec(arr, low, mid -1, x)
		else:
			return binary_searchRec(arr, mid+1, high, x)
	else:
		return -1

def binary_searchIter(arr, x): 
	low, high, mid = 0, len(arr)-1, 0
	while(low <= high): 
		mid = (high + low)//2
		if(arr[mid] < x):
			low = mid +1
		elif(arr[mid] > x):
			high = mid -1
		else: return mid 

	return -1


if __name__ == "__main__":
	l = [1,2,3,4,5,6,7,8,9,10]
	print(linear_search(l, 4))
	print(binary_search(l, 4))
	print(binary_searchRec(l, 0, 9, 4))
	print(binary_searchIter(l, 4))


