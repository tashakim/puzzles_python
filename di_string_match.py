class Solution(object):
    def diStringMatch(self, S):
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