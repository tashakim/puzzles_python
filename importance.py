def importance(array):
	array[:][3] = array[:][3]
	for i in range(0, 4):
		for j in range(0,3):
			for k in range(i-1, i+2):
				for l in range(j-1, j+2):
					if k>=0 and k<4 and l>=0 and l<3:
						array[i][j] += abs(array[k][l] - array[i][j])

	return array

def printArray(array) :
	print("The array is: ")

	for i in range(0,len(array)):
		for j in range(0,len(array[0])):
			print(array[i][j], end = " ")
		print()
	return

if __name__ == "__main__" :
	table = [[2,4,3,1], [5,2,1,4], [6,3,2,4], 
	[1,3,2,1]]

	print(len(table[0])) # prints number of columns
	print(len(table)) # prints number of rows

	#print(len([1,2,3,4]))
	printArray(table)
	print(table[:][3])

	print(importance(table))