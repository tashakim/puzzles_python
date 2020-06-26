"""Purpose: Returns all indices at which 'x' occurs in input list.
"""

def findInstances(L, x):
	if(not x in L): return [-1]
	res = []
	for i in range(len(L)):
		if(L[i] == x):
			res.append(i)
	return res


def findInstances2(L, x): 
	# Python list comprehension is generally faster than for-loop that builds a list.
	if(not x in L): return [-1]
	return [k for k in range(len(L)) if L[k] == x]

def findInstances3(L, x):
	if(x in L):
		return [k for k, y in enumerate(L) if y == x]
	else: return [-1]


if __name__ == "__main__":
	mylist, x = [64,72,88,72,54], 72

	assert(findInstances(mylist, x) == [1,3]), "Wrong answer."
	assert(findInstances(mylist, x) == findInstances2(mylist, x)), "Wrong answer."
	assert(findInstances3(mylist, x) == findInstances2(mylist, x)), "Wrong answer."

	print("All tests passed!")