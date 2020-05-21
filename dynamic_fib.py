def dynamic_fibonacci(n) :

	fib = []
	#fib.append(0)
	#fib.append(1)
	fib.extend([0,1])

	for i in range(2,n+1) :
		fib.insert(i, fib[i-1] + fib[i-2])
		print("fib[",i,"] is: ", fib[i])
	return fib[n]

for i in range(0,10):
	print(dynamic_fibonacci(i))
#dynamic_fibonacci(5)