def climbStairs(self, n):
	"""Purpose: Returns the number of distinct ways 
	one can climb n steps of stairs.
	Note: one can only take 1 or 2 steps at a time.
	"""
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def climbStairs2(self, n):
	a = b = 1
	for i in range(n-1): # watch the loop range
		a,b = b, a+b
	return b


"""What if you can take 1,2, or 3 steps at a time?"""

