def dynamic_factorial(n):
	fact = []
	fact.append(1)
	fact.append(1) 
	for i in range(2, n+1):
		fact.insert(i, i*fact[i-1])
	return fact.pop()

if __name__ == "__main__":
	print(dynamic_factorial(2))