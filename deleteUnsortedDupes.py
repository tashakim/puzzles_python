# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        res =[]
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        cache = collections.Counter(res)
        
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        while head:
            if cache[head.val] > 1:
                prev.next = head.next
            else:
                prev = prev.next          
            head = head.next

        return dummy.next