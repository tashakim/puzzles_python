def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


if __name__ == "__main__":
	print(largest_prime_factor(1000)) #5
	print(largest_prime_factor(7775460)) #17