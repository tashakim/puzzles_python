#Recursive vs iterative practice

def recfib(n):
	if(n == 0): return 0
	if(n == 1): return 1
	return recfib(n-1) + recfib(n-2)

def iterfib(n):
	if(n == 0): return 0
	if(n == 1): return 1
	counter = 2
	f0, f1 = 0,1
	while(counter <= n):
		f0, f1 = f1, f0 + f1
		counter +=1
	return f1

if __name__ == "__main__":
	print(recfib(5))
	print(iterfib(5))