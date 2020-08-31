import collections
class Solution:
    def validPalindrome1(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        my_bool = False
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if my_bool == False:
                    my_bool = True
                    # which one to delete?
                else:
                    return False
                
    def validPalindrome(self, s):
    """Purpose: Utilizing two pointers, starting at head and tail of string s
    respectively, checks validity of potential palindrome, 
    by excluding a character at a point of 'conflict'.

    Time complexity: O(n), where n is length of input string s.
    Space complexity: at the first point of 'conflict', we are creating new 
    temporary inverted windows with O(n) space - therefore
    O(2*n) = O(n) extra space is used.
    """
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                t1, t2 = s[:l]+s[l+1:], s[:r]+s[r+1:]
                return t1 == t1[::-1] or t2 == t2[::-1]
        return True