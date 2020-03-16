def print_to_n(n):
	if n<1:
		print("Invalid input: integer value cannot be less than 1")
		return
	for i in range(1, n+1):
		print(i)

if __name__ == "__main__" :
	print_to_n(3)