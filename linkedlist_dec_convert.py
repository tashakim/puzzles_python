# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	"""Time complexity: O(n),
	Space complexity: O(1).
	"""
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = res*2 + head.val
            head = head.next
        return res


class Solution2:
	"""Time complexity: O(n),
	Space complexity: O(1).
	"""
    def getDecimalValue(self, head: ListNode) -> int:
        res = ""
        while head:
            res += str(head.val)
            head = head.next
        return int(res,2)