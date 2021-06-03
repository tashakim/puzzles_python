# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        if not node:
            return None
        storage = {head.val:1}
        while node.next:
            node = node.next
            if node.val not in storage:
                storage[node.val] = 1
            else:
                storage[node.val] += 1
                
        res = head
        while head:
            while head.next and storage[head.next.val] >= 2:
                storage[head.next.val] -= 1
                head.next = head.next.next
            head = head.next
        
        return res