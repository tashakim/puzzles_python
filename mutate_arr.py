def mutateTheArray(n, a):

    b = [0]*n
    if n == 1:
        return [a[0]]
    b[0] = a[0] + a[1]
    b[-1] = a[-1] + a[-2]
    
    for i in range(1, n-1):
        b[i] = a[i-1] + a[i] + a[i+1]
    
    return b