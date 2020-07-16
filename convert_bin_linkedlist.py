# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
    """Purpose: Return the decimal value of the number
    that the linked list holds.
    """
        l = [head]
        while l[-1].next:
            l.append(l[-1].next) # O(n)
        
        n = len(l)
        res = 0
        for x in l:
            res += x.val*(2**(n-1)) # decimal conversion
            n -= 1
        return res