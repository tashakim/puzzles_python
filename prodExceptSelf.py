class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two-pass
        # one-pass using division (division by zero)
        # left_product * right_product
        left, right = [1], []
        left_prod = 1
        
        for i in range(1, len(nums)):
            left_prod *= nums[i-1]
            left.append(left_prod)
        right_prod = 1
        for i in reversed(range(len(nums)-1)):
            right_prod *= nums[i+1]
            right.append(right_prod)
            
        right.reverse()
        right.append(1)
        
        res = [0] * len(left)
        for i in range(len(left)):
            res[i] = left[i] * right[i]
            
        return res


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        res[0] = 1
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]

        R = 1
        for i in reversed(range(n)):
            res[i] *= R
            R *= nums[i]
            
        return res