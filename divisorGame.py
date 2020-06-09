def divisorGame(n):
	"""Purpose: Alice goes first, then Bob. 
	Choose any x s.t. 0 < x < n, and n%x ==0.
	Then replace n with n-x.
	If only Alice wins, return True. Else False.
	"""
	if(n%2 ==0):
		return True

	return False

if __name__ == "__main__":
	# prints results up to n = 9.
	for i in range(1, 10): 
		print("n is: ", i, "and result is: ,", divisorGame(i))
		
		# prints all divisors
		if(divisorGame(i) == True):
			divisors = []
			for div in range(1,i):
				if(i%div == 0):
					divisors.append(div)

			print("div = ", divisors)
