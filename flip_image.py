class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    """Purpose: Flips image horizontally, then inverts it.

    Time complexity: O(n*m), where n*m is the dimension of the image.
    Space complexity: O(n*m), where n*m is the dimension of the image.
    """
        dp = [[0]*len(A[0]) for row in A]
        for row in range(len(A)):
            for i in range(len(A[0])):
                dp[row][i] = A[row][-i-1] ^ 1
                
        return dp

       