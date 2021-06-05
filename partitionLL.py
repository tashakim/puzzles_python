# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solutions:
    def deleteDuplicateNode(self, head: ListNode) -> ListNode:
        # Purpose: Deletes a single duplicate node, if it exists.
        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
                return head
            cur = cur.next
        return head

    def deleteDuplicateNodes(self, head: ListNode) -> ListNode:
        # Purpose: Deletes all instances of duplicate nodes, in a sorted linked list.
        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    def deleteKthFromEnd(self, head: ListNode, k) -> ListNode:
        # Purpose: Deletes the kth node from the End of a linked list.
        ptr1, ptr2 = head, head
        for i in range(k):
            ptr1 = ptr.next

        if not ptr1: # deals with case where k == length of list
            return ptr2.next

        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr2.next = ptr2.next.next # performs deletion
        return head


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next