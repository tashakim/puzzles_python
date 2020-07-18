import timeit

class Solution:
    def runningSum(self, nums):
        """Purpose: Computes aggregate sum of array 'nums'.
        """
        sums = 0
        l = []
        for x in nums:
            sums += x
            l.append(sums)
        return l
    
    def runningSum2(self, nums):
        """Purpose: T.C: O(n), S.C: O(1).
        Q: Why is this method faster than runningSum() above?
        """
        i = 1
        while i<len(nums):
            nums[i] += nums[i-1]
            i += 1
        return nums


if __name__ == "__main__":
    setup = '''
    nums = [1,2,3,4,5]
    '''

    print(timeit.timeit(setup=setup, stmp= runningSum(nums)))