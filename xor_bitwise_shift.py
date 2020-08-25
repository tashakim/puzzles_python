class Solution:
    def xorOperation(self, n: int, start: int) -> int:
    """Purpose: Returns the bitwise XOR of all elements shifted
    by an increasing power of 2.
    """
        res = 0
        for i in range(n):
            res ^= start + 2*i
        return res 

    