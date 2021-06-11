import collections

def firstDuplicate(a):
    """
    Purpose: given array a that contains no.'s in range 1 to a.length, finds
    first duplicate no. for which second occurence has minimal index.
    """
    # Counter(a)
    c1 = collections.Counter(a)
    # get dupes = {elm in arr that has Counter >= 2 : arr.}
    dupes = {}
    for k, v in c1.items():
        if v >= 2 and k not in dupes:
            dupes[k] = 2
    print(dupes)
    # loop through a:
    idx = {}
    for i, x in enumerate(a):
        # if x in dupes:
        if x in dupes.keys() and dupes[x] > 0:
            dupes[x] -= 1
            idx[x] = i
            
    res = -1
    min_val = float('inf')
    for k, v in idx.items():
        if min_val > v:
            min_val = v
            res = k
            
    return res