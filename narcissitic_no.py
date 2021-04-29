def narcissistic( value ):
	"""
	Purpose: Returns bool indicating whether number is narcissistic or not.
	"""
    sum = 0
    val = str(value)
    for x in list(val):
        sum += int(x) ** len(val)
    return sum == value


def narcissistic( value ):
    l=list(str(value))
    n=len(l)
    sum = 0
    for item in l:
        sum += int(item)**n
    if(sum == value):
        return True
    else:
        return False