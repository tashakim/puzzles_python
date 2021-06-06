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


    def deleteKthFromEnd2(self, head: ListNode, k) -> ListNode:
        # Purpose: A two-pass solution to deleting kth node from the end of 
        # a linked list.
        length_of_list = 0
        cur = head 
        while cur.next:
            cur = cur.next
            length_of_list += 1
        n = length_of_list - k

        dummy = ListNode(-1, head)
        cur = dummy 
        while cur.next:
            if n == 0:
                cur.next = cur.next.next
                return dummy.next
            cur = cur.next
            k -= 1
        return dummy.next
        """ No sentinel node used:
        cur = head
        if n == 0:
            head = head.next
            return head
        while cur and cur.next:
            n -= 1
            if n == 0:
                cur.next = cur.next.next
                return head
            cur = cur.next
        return  head
        """


    def deleteCurNode(self, node: ListNode) -> ListNode:
        # Purpose: Without having access to the head node, delete the node 
        # that is passed in. It is guaranteed not to be a tail node.
        node.val = node.next.val # note: since node != self.tail, length_of_list must be larger than 1.
        node.next = node.next.next


    def removeValFromList(self, head: ListNode, val: int) -> ListNode:
        # Purpose: Removes all nodes that equals the value passed in.
        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
        """ Using previous pointer:
        dummy = ListNode(-1, head)
        prev = dummy
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next # head
        """


    def isPalindrome(self, head: ListNode) -> bool:
        # Purpose: Checks whether values in linked list forms a palindrome. 
        # Note space complexity is O(n), n = length 0f list.
        storage = []
        ptr = head

        while ptr:
            storage.append(ptr.val)
            ptr = ptr.next
        i = 0
        while i < len(storage) / 2:
            if storage[i] != storage[-i-1]:
                return False
            i += 1

        return True


    def isPalindrome(self, head: ListNode) -> bool:
        # Purpose: Checks if linked list forms a palindrome, with O(1) space complexity.
        self.head = head
        def recursiveCheck(cur = head):
            if cur:
                if not recursiveCheck(cur.next):
                    return False
                if self.head.val != cur.val:
                    return False
                self.head = self.head.next
            return True
        
        return recursiveCheck()


    def reverseList(self, head: ListNode) -> ListNode:
        # Purpose: Reverses the values in a linked list.
        prev = None # will become the val after TAIL node.
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev # return from the back


    def reverseList(self, head: ListNode) -> ListNode:
        # Purpose: Reverses the values in a linked list, WITHOUT multiple assignment.
        prev_node = None
        cur_node = head
        while cur_node:
            next_node = cur_node.next # copy over before we dismantle the bridge!
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = cur_node.next

        return prev_node 
        """
        head = prev_node
        return head
        """


    def reverseList(self, head: ListNode) -> ListNode:
        # Purpose: Reverses the values in a linked list, using an Array.
        # Space complexity is increased to O(n), n = length of linked list.
        storage = []
        cur = head
        while cur:
            storage.append(cur.val)
            cur = cur.val
        
        storage.reverse() # reversed_storage = list(reversed(storage))
        cur = head
        i = 0
        while cur:
            cur.val = storage[i] # don't reverse while looping! Save time.
            cur = cur.next
            i += 1
        return head


    def reverseList(self, head: ListNode) -> ListNode:
        # Purpose: Reverses the values in a linked list, recursively.
        if not head or if not head.next:
            return head
        res = self.reverselList(head.next) 
        head.next.next = head
        head.next = None
        return res


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lower_head = ListNode(0, head)
        higher_head = ListNode(0, head)
        lower = lower_head
        higher = higher_head

        while head:
            if head.val < x:
                lower.next = head
                lower = lower.next
            else:
                higher.next = head
                higher = higher.next
            head = head.next

        higher.next = None
        lower.next = lower_head.next

        return lower_head.next
