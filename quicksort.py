
def quickSortAscend(array):
	less = []
	equal = []
	greater = []

	if len(array) > 1:
		pivot = array[len(array)//2]

		for i in array:
			if i < pivot:
				less.append(i)
			if i == pivot:
				equal.append(i)
			if i > pivot:
				greater.append(i)

		return quickSortAscend(less) + equal + quickSortAscend(greater)
	else:
		return array


def quickSortDescend(array):
	less = []
	equal = []
	greater = []

	if len(array) > 1:
		pivot = array[len(array)//2]

		for i in array:
			if i < pivot:
				less.append(i)
			if i == pivot:
				equal.append(i)
			if i > pivot:
				greater.append(i)

		return quickSortAscend(greater) + equal + quickSortAscend(less)
	else:
		return array


if __name__ == "__main__":
	array = [8,3,1,19,3,77]
	print(quickSortAscend(array))
	print(quickSortDescend(array))
