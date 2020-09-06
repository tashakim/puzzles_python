def bubbleSort(dataset):
	"""Purpose:
	"""
	for i in range(len(dataset) -1, 0, -1):
		for j in range(i):
			if dataset[j] > dataset[j+1]:
				dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
		print("Current: ", dataset)
	
	return "sorted!"


def mergeSort(dataset):
	"""Purpose:
	- Divide - and - conquer algorithm
	- Breaks dataset into individual pieces, and merges them back together
	- Uses recursion!
	- Performs well on large sets of data 
	- Time complexity: O(n log(n))
	"""


if __name__ == "__main__":
	bubbleSort([4,2,5,3,1])
	