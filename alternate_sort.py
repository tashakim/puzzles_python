def alternatingSort(a):
    """Purpose: Returns a sorted array merged with a special rule.
    """
    cur, prev = 0, float('-inf')
    for i in range(len(a)):
        print("i = ", i)
        if i%2 == 0: # even index
            cur = i//2
        else: # odd index
            cur = (-i//2) 
        if a[cur] <= prev:
            return False
        prev = a[cur]
    return True