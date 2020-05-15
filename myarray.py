myArray = [0]*5

print(myArray)

grid = [[1,2,3], [1,2,3], [1,2,3]]

# we have a 3x3 array.
print(grid)

# we can print it like this
for line in grid:
	for ele in line:
		print(ele, end = " ")
	print()
""" Note: By default, python's print() function 
ends with a newline!
"""

# let's print the 1x3 element!
print("1x3 element is: ", grid[0][2])

# let's print the 2x2 element!
print("2x2 element is: ", grid[1][1])