def insert_sort(array):
	for i in range(1, len(array)):
		key = array[i]

		j = i-1
		while j>= and array[j] > key:
			array[j+1] = array[j]
			j -= 1

		array[j+1] = key

	return array

if __name__ == "__main__":
	