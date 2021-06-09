# Can you check if the letter value sum of two words equal the third?
def letterWordsEq(first, second, res):
	# The ordinal of a lowercase alphabet - 97 is equal to 0.
	a = [str(ord(x) - 97) for x in first]
	b = [str(ord(x) - 97) for x in second]
	c = [str(ord(x) - 97) for x in res]

	return int(''.join(a)) + int(''.join(b)) == int(''.join(c))

def letterWordsEq2(first, second, res):
	# All in one line
	return int(''.join([str(ord(x) - 97) for x in first])) + int(''.join([str(ord(x) - 97) for x in second])) == int(''.join([str(ord(x) - 97) for x in res]))