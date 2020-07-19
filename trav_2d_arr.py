def setup():
	"""Purpose: Defines array to be used in traversals.
	"""
	a = [[1,2,3],[4,5,6],[7,8,9]]
	traverseArr(a)
	print()
	traverseArr2(a)
	print()


def traverseArr(arr):
	"""Purpose: Uses indices to print 2d array.
	"""
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			print(arr[i][j], end = " ")
		print()

def traverseArr2(arr):
	"""Purpose: Uses items to print 2d array.
	"""
	for row in arr:
		for el in row:
			print(el, end = " ")
		print()

class Solution:
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            for el in row:
                if el < 0:
                    count +=1
        return count


if __name__ == "__main__":
	setup()

	assert(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]) == 8), "Wrong answer"
	print("Test passed!")