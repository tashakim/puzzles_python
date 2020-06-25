import time
"""Purpose: Compares the time elapsed for various ways of 
inserting item into sorted list.
"""

def insertSorted(L, x): # fastest method
	for i in range(len(L)):
		if(x <= L[i]):
			L.insert(i, x)
			return L
	L.append(x)
	return L

def insertSorted2(L, x): # slowest method
	for item in L:
		if(x <= item):
			print("why are you here")
			L.insert(L.index(item), x)
			return L
	L.append(x)
	return L

def insertSorted3(L, x): # 2nd fastest
	for i, val in enumerate(L):
		if(x <= val):
			L.insert(i, x)
			return L
	L.append(x)
	return L


if __name__ == "__main__":
	mylist = [20,37,58,72,91]
	val = 100

	ts = time.time()
	print("Result is: ", insertSorted(mylist, val))
	elapsed = time.time() - ts
	print("The elapsed time for insertSorted is: %.7f" % elapsed)
	mylist.pop()

	ts = time.time()
	print("Result is: ", insertSorted2(mylist, val))
	elapsed = time.time() - ts
	print("The elapsed time for insertSorted2 is: %.7f" % elapsed)

	ts = time.time()
	print(insertSorted3(mylist, val))
	elapsed = time.time() - ts
	print("The elapsed time for insertSorted3 is: %.7f" % elapsed)
