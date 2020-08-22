class Solution:
    def longestPalindrome(self, s: str) -> str:
    """Purpose: Returns the palindromic substring with max length.
    Note: Expands around the center at each step of traversing string s.
    """
        def helper(s, left, right):
            """Purpose: Helper method that returns the longest palindromic 
            substring starting at a specific index.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # returns the longest palindromic substring starting at index i
            return s[left +1: right]
            
        sub = ""
        for i in range(0, len(s)):
            odd = helper(s, i, i)
            even = helper(s, i, i+1)
            sub = max(odd, even, sub, key = len) # return max by length of substring
            
        return sub