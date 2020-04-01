def rec_factorial(n):
	if n == 0:
		return 1
	return helper(n)

def helper(n):
	if n==1:
		return 1
	if n>1:
		return n*helper(n-1)

def test():
	assert rec_factorial(3) == 6, "Test failed"
	assert rec_factorial(0) == 1, "Test failed"
	assert rec_factorial(1) == 1, "Test failed"
	

if __name__ == "__main__":
	print(rec_factorial(2))
	test()