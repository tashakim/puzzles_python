class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Purpose: Returns the minimum element of a rotated array `nums` of unique integers.

        This solution uses binary search, to improve time complexity to O(log(n)), where n is the 
        number of elements in the array.
        
        """
        low, high = 0, len(nums) - 1

        while nums[low] > nums[high]:
            mid  = (low + high)//2

            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1

        return nums[low]


    def findMin(self, nums: List[int]) -> int:
        """
        Purpose: Linear time solution. 
        """
        return min(nums)