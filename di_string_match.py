class Solution(object):
    def diStringMatch(self, S):
        """Purpose: 'I' signifies increase, whereas 'D' signifies decrease.
        Return any permutation of numbers [0,1, ..., N] s.t. 
            if S[i] == 'I' then A[i] < A[i+1], and
            if S[i] == 'D' then A[i] > A[i+1].

        """
        lo, hi = 0, len(S)
        res = []
        for x in S:
            if x == 'I':
                res.append(lo)
                lo += 1
            else:
                res.append(hi)
                hi -= 1
        res.append(lo)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.diStringMatch("IDID"))
    print(s.diStringMatch("III"))
    print(s.diStringMatch("DDI"))