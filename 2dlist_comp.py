def twoDlist_comp(x,y, N):
	"""Purpose: prints out all coordinates [x,y]
	such that x+y does not equal N.
	"""
	coordinates = []
	for i in range(x+1):
		for j in range(y+1):
			if(i+j!= N):
				coordinates.append([i,j])

	print(coordinates)


if __name__ == "__main__":
	twoDlist_comp(1,1,2)
	twoDlist_comp(2,3,4)