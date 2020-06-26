import time
"""Purpose: Compares the time elapsed for various ways of 
inserting item into sorted list.
"""

def insertSorted(L, x): # Corrected: fastest.
	for i in range(len(L)):
		if(x <= L[i]):
			L.insert(i, x)
			return L
	L.append(x)
	return L

def insertSorted2(L, x): # fastest method: 0.0000057s
	for item in L:
		if(x <= item):
			L.insert(L.index(item), x)
			return L
	L.append(x)
	return L

def insertSorted3(L, x): # 2nd fastest: 0.0000060s
	for i, val in enumerate(L):
		if(x <= val):
			L.insert(i, x)
			return L
	L.append(x)
	return L

def insertSorted4(L, x): # 4th: 0.0000069s
	L.insert([k for k in range(len(L)) if x > L[k]].pop()+1, x)
	return L

def insertSorted5(L,x): # 3rd: 0.0000060s Why is len() faster than pop()?
	L.insert(len([k for k in range(len(L)) if x > L[k]]), x)
	return L


if __name__ == "__main__":
	mylist = [20,37,58,72,91]
	val = 100

	tests = [insertSorted, insertSorted2, insertSorted3, insertSorted4, insertSorted5]
	# First test runs way slower than the others. Due to various reasons.
	# Change around the order of tests to see.
	for i in range(5):
		ts = time.time()
		print("Result: ", tests[i](mylist, val))
		elapsed = time.time() - ts
		print("The elapsed time for insertedSort",i+1, "is: %.7f" % elapsed)
		mylist.pop()
	
	print("All tests completed")