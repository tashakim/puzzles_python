# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """Purpose: Checks if linked list values form a palindrome.

        Stores all values of linked list in an array,
        then reverses the array.
        """
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

    def isPalindrome(self, head):
        """Purpose: Same as above, but with improved space complexity.

        In-place solution, using slow & fast 
        pointers to find middle point efficiently.
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
            
        return not rev