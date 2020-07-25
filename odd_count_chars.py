class Solution:
    def generateTheString(self, n: int) -> str:
    """Purpose: Simple. Returns a string with n characters such that 
    each character in such string occurs an odd number of times.
    """
        if n%2 == 1:
            return 'a'*n
        else:
            return 'a'*(n-1) +'b'