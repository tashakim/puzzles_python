# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # two-pass solution
        length_of_list = 1
        cur = head
        while cur.next:
            cur = cur.next
            length_of_list +=1
        k = length_of_list - n
        
        cur = head
        if k == 0:
            head = head.next
            return head
        
        while cur and cur.next:
            k -= 1
            if k == 0:
                cur.next = cur.next.next
                return head
            cur = cur.next
        return head


    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr1, ptr2 = head, head
        for i in range(n): ptr1 = ptr1.next
        if not ptr1: return ptr2.next
        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = ptr2.next.next
        return head
        
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        ptr1, ptr2 = dummy, dummy
        for i in range(n): 
            ptr1 = ptr1.next

        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = ptr2.next.next
        return head
        