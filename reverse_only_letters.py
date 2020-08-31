class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
    """Time complexity: O(n), where n is length of input string S.
    Space complexity: O(n), strings are immutable, so we created a new list 
    with n elements, where n is length of input string S.
    """
        i = 0
        j = len(S)-1
        S = list(S)
        while i < j:
            while not S[i].isalpha() and i < j:
                i += 1
            while not S[j].isalpha() and i < j:
                j -=1
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1
        return "".join(S)