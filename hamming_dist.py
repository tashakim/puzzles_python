class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
    """Purpose: Computes Hamming Distance between two integers, x and y.

    Definition: Hamming Distance compares two binary data strings, then 
    computes the number of bit positions in which two bits are different.
    """
        s = str(bin(x^y)[2:])
        return s.count('1')