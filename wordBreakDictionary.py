from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Purpose: Returns whether input string `s` can be segmented into a space-separated
        sequence of one or more dictionary words in `wordDict`.
        """
        self.mybool = False
        @lru_cache
        def helper(s):
            i = 0
            cur = ""
            while i < len(s):
                cur += s[i]
                if cur in wordDict:
                    if i >= len(s)-1: 
                        self.mybool = True
                        return
                    helper(s[i+1:])
                i += 1
        helper(s)
        return self.mybool