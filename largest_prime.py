def largest_prime_factor(n):
	"""Purpose: Returns the largest prime factor of 'n'.
	"""
	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
	return n
	

def all_prime_factors(n):
	"""Purpose: Returns a list of all prime factors of 'n'.
	"""
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors


if __name__ == "__main__":
	print(largest_prime_factor(1000)) #should print 5
	print(all_prime_factors(1000))

	print(largest_prime_factor(7775460)) #should print 17
	print(all_prime_factors(7775460))