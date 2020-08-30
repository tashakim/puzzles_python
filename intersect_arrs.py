import collections

class Solution:
    def intersect0(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Time complexity: O(n), where m is the number of elements in nums1.
        Space complexity: O(m), where n is the number of elements in nums2.
        """
        res = []
        ht = collections.Counter(nums2)
        for item in nums1:
            if item in ht and ht[item] > 0:
                ht[item] -= 1
                res.append(item)
                
        return res
    
    def intersect(self, nums1, nums2):
        """Assumption: input arrays nums1 and nums2 are already sorted.
        Time complexity: O(m+n), where m and n are length of arrays nums1, nums2 respectivetly.
        Space complexity: O(1) Improvement on space complexity!
        """
        # if the arrays are already sorted:
        nums1.sort()
        nums2.sort()
        
        # let p1, p2 be pointers at the beginning of nums1 & nums2.
        p1, p2 = 0,0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return res

class Solution:
    """Purpose: Similar issue, the problem is to find intersection of two arrays,
    not accounting for duplicates.
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Time complexity: O(n*m) worst case, where n, m are length of arrays nums1, nums2 respectively.
        Space complexity: O(max(n, m)) worst case.
        """
        return [x for x in set(nums1) if x in set(nums2)]
    
    
    def intersection(self, nums1, nums2):
        """Constraint: O(n) time, O(1) space. Lists are sorted.

        Time complexity: O(n+m) worst case, n,m are lengths of nums1, nums2 respectively. 
        Space complexity: O(1)! Improvement from first method.
        """
        nums1.sort()
        nums2.sort()
        
        p1 = 0 # points to start of nums1
        p2 = 0 # points to start of nums2
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return set(res)
        