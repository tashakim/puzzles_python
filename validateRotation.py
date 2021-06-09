# Can you determine whether a target matrix can be obtained by rotating a given matrix any number of times?
def checkValidRotation(arr, target):
	# Checks if target matrix can be obtained iteratively
	def rotate(arr, target):
		arr.reverse()
		for i in range(len(arr)):
			for j in range(i, len(arr)):
				arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

		return arr

	if arr == target: return True
	arr2 = rotate(arr)
	if arr2 == target: return True
	arr3 = rotate(arr2)
	if arr3 == target: return True
	arr4 = rotate(arr3)
	if arr4 == target: return True

	return False

def checkValidRotation2(arr, target):
	# We could also keep track of a boolean that ticks True when we obtain target matrix.
	self.bool = False
	def check(arr, target):
		arr.reverse()
		for i in range(len(arr)):
			for j in range(i, len(arr)):
				arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
		if arr == target: self.bool = True
		return arr

	if arr == target: return True
	for i in range(3):
		rotate(arr)
	return self.bool