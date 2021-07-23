# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        Purpose: Sorts the values of a linked list using insertion sort, 
        returns the linked list's head node.

        O(n) space complexity, where n is no. of nodes in linked list.
        """
        dummy = head
        cur = head
        cache = []
        while cur:
            cache.append(cur.val)
            cur = cur.next
        cache.sort()
        
        i = 0
        while head:
            head.val = cache[i]
            i += 1
            head = head.next
            
        return dummy


    def insertionSortListw(self, head: ListNode) -> ListNode:
        """
        Solution improves space complexity.
        """
        pass