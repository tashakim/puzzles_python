class Solution:
    def reverse(self, x: int) -> int:    
    """Purpose: Reverses the digits of a 32-bit signed integer.

    Note: Assume we may only store integers within 32-bit signed
    integer range [-2^31, 2^31 - 1].

    Example: -123 -> -321
    1234 -> 4321
    120 -> 21
    """ 
        sign = 1
        if x < 0:
            sign = -1
            s = str(x)[1:]
        else:
            s = str(x)
        res = int(s[::-1])
        if not res > 2**31:
            return res*sign
        return 0
        