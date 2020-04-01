def rec_factorial(n):
	return helper(n)

def helper(n):
	if n==1:
		return 1
	if n>1:
		return n*helper(n-1)
	

if __name__ == "__main__":
	print(rec_factorial(2))
	assert rec_factorial(3) == 6, "Test failed"