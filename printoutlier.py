def find_outlier(integers):
	"""Purpose: 
	"""
    d = {}
    v = [None]*len(integers)
    
    for i in range(len(integers)):
        d[integers[i]] = integers[i]%2
        v[i] = integers[i]%2
        
    if(sum(v) > 1):
        return list(d.keys())[list(d.values()).index(0)]
    else:
        return list(d.keys())[list(d.values()).index(1)]
