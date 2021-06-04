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


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # T: O(n), S: O(n)
        node = head
        if not node: return None
        storage = defaultdict(lambda: 0)

        while node:
            storage[node.val] += 1
            node = node.next
                
        res = head
        while head:
            while head.next and storage[head.next.val] >= 2:
                storage[head.next.val] -= 1
                head.next = head.next.next
            head = head.next
        
        return res
    

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # The input is guaranteed to be sorted, S: O(1)
        if not head: return None
        res = head
        while head:
            cmp = head
            while head.next and head.next.val == cmp.val:
                head.next = head.next.next
            head = head.next
        
        return res

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Practise using a dummy pointer, S: O(1)
        if not head: return None
        dummy = ListNode('Dummy', head)
        cur = dummy
        while cur.next:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

        