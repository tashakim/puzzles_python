def bin(n) :
	bins = []
	binhelper(bins, n)

	num = bins.count(1)
	return num


def binhelper(bins, n) :
	if n>1:
		binhelper(bins, n//2)
	bins.append(n%2)
	return bins


print(bin(3))