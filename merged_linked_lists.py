# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	"""Purpose: Returns the node at which two singly linked lists
	merge. 
	This solution uses two pointers, which is an
	improvement from O(n) memory using a hash table.
	"""
    def getIntersectionNode(self, headA, headB):
        if headA and headB:
            p1, p2 = headA, headB
            while p1 != p2:
                p1 = headB if p1 is None else p1.next
                p2 = headA if p2 is None else p2.next
                
            return p1

