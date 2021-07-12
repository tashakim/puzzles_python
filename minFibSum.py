class Solution:
    def uniqueFibSum(self, k:int):
        """
        Purpose: Returns the min. number of Fibonacci numbers  whose sum equals k.
        Same Fibonacci number can be used multiple times.
        """
        self.count = 0

        def recurse(k):
            if k==0 or k==1:
                return k
            
            a, b = 1, 1
            i = 2
            while b < k:
                a, b = b, a + b
            k -= a
            self.count += 1
            return recurse(k)

        recurse(k)

        return self.count