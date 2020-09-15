class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    	"""Purpose: Given two integer arrays of equal length 
    	target, arr,
    	select any non-empty subarry of arr and reverse it, any
    	number of steps.
    	Return boolean indicating whether arr equals to target.

    	Example: target=[1,2,3,4], arr=[2,4,1,3] => True
    	
    	"""
        return collections.Counter(target) == collections.Counter(arr)