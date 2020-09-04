class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum([self.data[i]*vec.data[i] for i in range(len(self.data))])
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)