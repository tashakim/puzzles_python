def argmax(L,f):
	l = [f(x) for x in L]
	print("f(x) = ", l)
	return L[l.index(max(l))]
	
def func(x):
	return x*2

def func2(x):
	return x-3

def func3(x):
	return 1/x

if __name__ == "__main__":
	arr = [1,2,3]

	assert(argmax(arr, func) == 3), "Error"
	assert(argmax(arr, func2) == 3), "Error"
	assert(argmax(arr, func3) == 1), "Error"

	print("All tests passed!")