def dynamic_factorial(n):
	fact = []
	fact.append(1)
	if n == 0:
		return fact.pop()
	fact.append(1) 
	if n==1:
		return fact.pop()
	for i in range(2, n+1):
		fact.insert(i, i*fact[i-1])
	return fact.pop()

def test():
	assert dynamic_factorial(3) == 6, "Test failed"
	assert dynamic_factorial(0) == 1, "Test failed"
	assert dynamic_factorial(1) == 1, "Test failed"
	print("Success!")

if __name__ == "__main__":
	print(dynamic_factorial(2))
	test()