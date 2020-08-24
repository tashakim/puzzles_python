class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
    """Purpose: Computes Hamming Distance between two integers, x and y.

    Definition: Hamming Distance compares two binary data strings, then 
    computes the number of bit positions in which two bits are different.
    """
        s = str(bin(x^y)[2:])

        return s.count('1')

def test():
	assert(hammingDistance(0,0) == 0), "Hamming distance between two equal integers equal zero."

	assert(hammingDistance(0,4) == 1), "Hamming distance between zero and another integer equal the number of 1's in its binary representation."
	
	assert(hammingDistance(1,4) == 2), "Wrong answer"
	assert(hammingDistance(200,400) == 4), "Wrong answer"
	assert(hammingDistance(0,1015) == 9), "Wrong answer"


if __name__ == "__main__":
	test()
	print("All tests passed!")