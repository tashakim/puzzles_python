class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]
        return

class Solution1:
	def rotate(self, nums: List[int], k: int) -> None:
		"""
		Purpose: Utilizes a helper method to rotate the input array.
		"""
		def reverseOne(nums):
            a = nums
            return [a[-1]] + a[:-1]
        
        for i in range(k):
            nums[:] = reverseOne(nums)

         return

if __name__ == "__main__":
	nums = [1,2,3,4,5,6,7]
	nums1 = [-1,-100,3,99]

	s.Solution()
	assert(s.rotate(nums, 3) == [5,6,7,1,2,3,4]), "Wrong answer"
	assert(s.rotate(nums1, 2) == [3,99,-1,-100]), "Wrong answer"

	s1.Solution()
	assert(s.rotate(nums, 3) == s1.rotate(nums, 3)), "Wrong answer"
	assert(s.rotate(num1, 2) == s1.rotate(num1, 2)), "Wrong answer"

	print("All tests passed!")