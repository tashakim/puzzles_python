class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
    """Purpose: Groups 2n integers into n pairs, then takes
    the min value and sums across all n pairs.

    Quick solution
    """
        return sum(sorted(nums)[::2])