class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # Time: O(n)
        start, end = 0, len(A)-1
        res = []
        while start <= end:
            if A[start] ** 2 > A[end] ** 2:
                res.append(A[start] ** 2)
                start += 1
            elif A[start] ** 2 <= A[end] ** 2:
                res.append(A[end] ** 2)
                end -= 1
        
        return res[::-1]

    def sortedSquares(self, A):
        return sorted[x**2 for x in A]