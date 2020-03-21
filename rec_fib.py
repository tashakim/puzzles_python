def rec_fibonacci(n) :
	
	if n == 0:
		return 0
	elif n == 1:
		return 1

	return rec_fibonacci(n-1) + rec_fibonacci(n-2)

for i in range(0, 10):
	print(rec_fibonacci(i))
