class Solution:
    def findKthLargest(self, nums, k):
    """Purpose: Returns the kth largest item of an unsorted array,
    using Quickselect.
    """
        def partition(l, r, i):
            pivot = nums[i]
            nums[i], nums[r] = nums[r], nums[i]  
            index = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[index], nums[i] = nums[i], nums[index]
                    index += 1

            nums[r], nums[index] = nums[index], nums[r]  
            return index
        
        def select(l, r, k_smallest):
            if l == r:       
                return nums[l]   
            i = random.randint(l, r)     
            i = partition(l, r, i)
            
            if k_smallest == i:
                 return nums[k_smallest]
            elif k_smallest < i:
                return select(l, i - 1, k_smallest)
            else:
                return select(i + 1, r, k_smallest)
        return select(0, len(nums) - 1, len(nums) - k)
            