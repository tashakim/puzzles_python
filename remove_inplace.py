class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    """Purpose: Remove all instances of input val, and returns the 
    new length and array num.

    Note: We do this by not allocating extra space for another array. 
    Therefore, we modify the input array in-place with O(1) space.
    """
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i