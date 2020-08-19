# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    
class Solution(object):
    def removeElements(self, head, k):
    """Purpose: Removes all elements from linked list equal to k
    """
        dummy = ListNode(-1) # dummy head for edge cases.
        dummy.next = head
        
        cur = dummy
        while cur.next:
            if cur.next.val == k: 
                cur.next = cur.next.next # skip over cur.next
            else:
                cur = cur.next # keep traversing if != k.

        return head