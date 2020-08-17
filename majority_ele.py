import collections

class Solution:
	"""Purpose: Utilizes the collections module to calculate
	the majority element in the input array.
	"""
    def majorityElement(self, nums: List[int]) -> int:
        mydict = collections.Counter(nums)
        for k, v in mydict.items():
            if v > math.floor(len(nums)/2):
                return k
        

if __name__ == "__main__":
	s = Solution()
	assert(s.majorityElement([3,2,3]) == 3), "Wrong answer"
	assert(s.majorityElement([2,2,1,1,1,2,2]) == 2), "Wrong answer"

	print("All tests passed!") 