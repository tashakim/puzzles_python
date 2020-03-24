def dynamic_fib(n) :
	fibs = []
	fibs.append(0)
	fibs.append(1)

	for i in range(2, n+1):
		fibs.insert(i, fibs[i-1]+ fibs[i-2])
	return fibs[n]


for i in range(6):
	print(dynamic_fib(i))

