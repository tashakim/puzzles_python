def tdlist_comp(x,y, N):
	"""Purpose: prints out all coordinates [x,y]
	such that x+y does not equal N.
	"""
	coordinates = []
	for i in range(x+1):
		for j in range(y+1):
			if(i+j!= N):
				coordinates.append([i,j])

	print(coordinates)


def thdlist_comp(x,y,z,N):
	"""Purpose: prints out all coordinates [x,y,z] 
	such that x+y+z   does not equal N.
	"""
	coordinates = []
	for i in range(x+1):
		for j in range(y+1):
			for k in range(z+1):
				if(i+j+k!=N):
					coordinates.append([i,j,k])
	print(coordinates)


if __name__ == "__main__":
	print("two-dim list comp: \n")
	tdlist_comp(1,1,2)
	tdlist_comp(2,3,4)
	print()

	print("three-dim list comp: \n")
	thdlist_comp(1,1,1,2)
	thdlist_comp(2,2,2,4)
	print()
