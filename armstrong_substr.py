class Solution:
    def isArmstrong(self, N: int) -> bool:
    """Purpose: Checks if an integer N is an Armstrong 
    number; i.e., the k-th power of each digit sums to N.
    """
        k = len(str(N))
        arm_num = 0
        for d in str(N):
            arm_num += int(d)**k
        return arm_num == N
        

class Solution:
    def countLetters(self, S: str) -> int:
    """Purpose: Returns the number of substrings of string
    S that have only one distinct letter.
    """
        start = S[0]
        count, res = 0, 0
        for c in S:
            if start == c:
                count += 1
            elif start != c:
                res += count*(count+1)//2
                start = c
                count = 1
        res += count*(count+1)//2
        return res