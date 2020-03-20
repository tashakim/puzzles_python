def sumofArray(array):
	if len(array) == 0:
		print('error')
	else:
		sum = 0
		for i in range(len(array)-1):
			sum += array[i]
		return sum


print(sumofArray([1,2,3]))