class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        Purpose: Returns the min. no. of flips to make string `s` monotonic increasing.

        """
        zero_count = s.count('0')
        one_count = 0
        
        res = len(s) - one_count

        for i in range(len(s)):
            if s[i] == '0': 
                zero_count -= 1
            elif s[i] == '1':
                res = min(res, zero_count + one_count)
                one_count += 1
                
        return res