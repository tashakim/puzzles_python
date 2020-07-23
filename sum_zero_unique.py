class Solution:
    def sumZero(self, n: int) -> List[int]:
    """Purpose: Return any array containing 'n' unique 
    integers such that they all add up to 0.
    """
        l = [x for x in range(1,n//2+1)] + [-x for x in range(1,n//2+1)]
        if n%2 == 1:
            return l + [0]
        else:
            return l

    def sumZero2(self, n: int) -> List[int]:
    """Purpose: This solution also works.
    """
        l = [x for x in range(0,n-1)]
        l += [-1*sum(l)]
        return l