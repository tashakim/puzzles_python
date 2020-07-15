# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    """Purpose: Reverses a linked list iteratively.
    Example: 
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
    Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
    """
        prev = None # initialize prev
        while head: 
            curr = head # starting point
            head = head.next # move head along to tail
            curr.next = prev # reverse link
            prev = curr # move prev forward
            
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
    """Purpose: Reverses a linked list recursively.
    Example: 
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
    Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
    """
    	return self.helper(head)

    def helper(self, node, prev = None):
    	if not node:
    		return prev
    	n = node.next
    	node.next = prev
    	return self.reverse(n, node)


    def reverseList3(self, head):
   	"""Purpose: Shorter solution, equivalent to reverseList().
   	"""
   	curr, prev = head, None
   	while curr:
   		curr.next, prev, cur = prev, curr, curr.next
   	return prev

   	