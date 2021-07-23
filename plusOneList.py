class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head:ListNode) -> ListNode:
        """
        Purpose: Adds one to a positive integer represented as a linked list of digits.

        Case 1: last digit is NOT 9, increase the right-most digit.
            [1, 9, 0] -> [1, 9, 1]

        Case 2: last digit is 9, increase the right-most non 9.
            [1, 1, 9] -> [1, 2, 0]

        Case 3: dummy.val (0) + 1, increase in no. of digits, rest are set to 0.
            [9, 9] -> [1, 0, 0]

        """
        dummy = ListNode(0) # important! set init val to 0.
        dummy.next = head
        digit = head

        while head:
            if not_nine != 9:
                not_nine.val = head
            head = head.next

        digit.val += 1
        digit = digit.next

        while digit:
            digit.val = 0
            digit = digit.next

        return dummy if dummy.val == 0 else dummy.next