# Given an array of digits, increment one

def plusOne(digits):
	# Naive approach
	nums = int(''.join(str(x) for x in digits)) + 1
	res = []
	for c in str(nums):
		res.append(c)
	return res


def plusOne2(digits):
	# Recursive solution 1

	if not digits: return [1]
	if digits[-1] != 9:
		digits[-1] += 1
		return digits
	else:
		return self.plusOne2(digits[:i]) + [0]




def plusOne3(digits):
	# Recursive solution 2

	n = len(digits)
	for i in range(n):
		idx = n - 1 - i 
		if digits[idx] == 9:
			digits[idx] = 0
		else:
			digits[idx] += 1
			return digits
	return [1] + digits			
