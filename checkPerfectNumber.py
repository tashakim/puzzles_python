class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        Purpose: Returns whether input num is a perfect number.
        A `perfect number` is a positive integer that is equal to the sum of its positive divisors,
        excluding the number itself.
        """
        def getDivisors(num):
            res = 0
            for i in range(1, math.ceil(math.sqrt(num))):
                if num%i==0:
                    res+=i+num/i
            return res

        return getDivisors(num) == num*2

    def checkPerfectNumber(self, num: int) -> bool:
        """
        """
        def getDivisors(num):
            res = 0
            for i in range(1, math.ceil(math.sqrt(num))):
                if num%i==0:
                    res+=i
                    res+=(num/i)
            return res
        
        a = getDivisors(num)

        return a == num * 2