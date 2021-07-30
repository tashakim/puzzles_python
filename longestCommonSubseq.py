from collections import Counter
class Solution:
    def longestCommomSubsequence(self, arrays):
        """
        Purpose: Returns an integer array with the longest common subsequence bw all arrays in 
        input arrays, which are sorted in strictly increasing order.
        """
        res = []
        for x in arrays:
            res += x
        c = Counter(res)

        return [k for k,v in c.items() if v == len(arrays)]

        # one-liner:
        # return [k for k,v in Counter(x for arr in arrays for x in arr).items() if v == len(arrays)]