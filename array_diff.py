def array_diff(a, b):
	"""
	Purpose: Deletes array diff.
	"""
    for i, x in enumerate(a):
        if x in b:
            a[i] = None
    res = []
    for x in a:    
        if x is not None:
            res.append(x)
    return res

def array_diff2(a, b):
    for ele in b:
        while ele in a:    
            a.remove(ele)
    return a


def array_diff3(a, b):
   return [i for i in a if i not in b]