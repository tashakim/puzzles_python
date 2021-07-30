# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Purpose: Brute force solution, loop through k lists storing all values.
        Sort all values, then create resulting linked list with ascending order.

        Space Complexity: O(n_1 + n_2 + n_3, ...) where n_1 is length of list 1, ... n_k is length of list k.
        """
        res = []
        def store_values(start):
            cache = []
            while start:
                cache.append(start.val)
                start = start.next
            return cache
        
        for L in lists:
            res += store_values(L)
        
        res.sort()
        res.reverse()
        
        dummy = ListNode(-1)
        cur = dummy
        
        while res:
            popped = res.pop()
            cur.next = ListNode(val=popped)
            cur = cur.next
            
        return dummy.next


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Purpose: Solution using a priority queue to store values in k lists.
        """
        pass
