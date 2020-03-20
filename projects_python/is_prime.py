def add(x,y):
	return x+y

def is_prime(n):
	if n<2:
		print("n must be greater than 1")
		return

	if n == 2:
		return True

	for i in range(2, n//2+1):
		if (n%i) == 0:
			return False
	return True
	

def test_is_prime(n):
	assert is_prime(2) == True, "Test failed: 2 is prime number"
	assert is_prime(19) == True, "Test failed: 19 is prime number"



if __name__ == "__main__":
	assert add(2,3) == 5, "Arithmetic failure! Try again"
	print(is_prime(3))
	print(is_prime(4))
	print(is_prime(6))
