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


    def areOccurrencesEqual(self, s: str) -> bool:
        """
        Purpose: Returns Boolean indicating whether all chars that appear in s have the same no. 
        of occurrences in string s.
        """
        c = Counter(s)
        return len([k for k,v in c.items() if v == len(s)//len(c)]) == len(c)


    def canBeTypedWords(self, text, brokenLetters):
        """
        Purpose: Returns the no. of words in `text` of words (separated by a single space) that you can 
        fully type using a broken keyboard that contains the letters in `brokenLetters`.
        """
        count = 0
        words = text.split(' ')
        for word in words:
            if all([c not in word for c in brokenLetters]):
                count += 1
        return count