class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Purpose: Returns a peak element in an integer array, which is an element 
        that is strictly greater than its neighbors.        
        """
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[mid+1]: # check slope, then narrow down window
                high = mid 
            else:
                low = mid + 1
        return low

    def findPeakElement1(self, nums):
        """
        Utilizing the fact we're looking for a 'local maximum' element, 
        we can also terminate searching as soon as we find a non-monotonic sequence.

        """
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return i - 1
        return len(nums)-1


    def findPeakElement2(self, nums):
        # one-liner python solution
        return nums.index(max(nums))