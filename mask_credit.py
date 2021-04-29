def maskify(cc):
	"""
	Purpose: Maskifies credit card no.
	"""
    n = len(cc)
    res = '#'*(n-4)
    if n >= 4:
        return res + cc[-4:]
    else:
        return cc


def maskify2(cc):
    return "#"*(len(cc)-4) + cc[-4:]


def maskify3(cc):
    word = list(cc)
    for i in range(len(word)-4):
        word[i] = '#'
        
    return ''.join(word)