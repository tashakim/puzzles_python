# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy.next
        valueList = []
        while cur:
            valueList.append(cur.val)
            cur = cur.next
        
        head = 0
        tail = len(valueList) -1
        while head < tail:
            if valueList[head] != valueList[tail]:
                return False
            head += 1
            tail -= 1
        return True