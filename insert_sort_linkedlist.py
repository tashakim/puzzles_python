# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortLinkedList(self, head: ListNode) -> ListNode:
    	"""
    	Purpose: Returns a sorted linked list using the insertion sort algorithm.

    	Time Complexity: O(n^2), where n is no. of nodes in linked list.
    	Space Complexity: O(1), does not use additional storage.
    	"""
        psuedo = ListNode()
        cur = head
        while cur:
        	prev = psuedo
        	next = prev.next
        	while next:
        		if cur.val < next.val:
        			break
        		prev = next
        		next = next.next

        	temp = cur.next
        	cur.next = next
        	prev.next = cur

        	cur = temp
        return psuedo.next


if __name__ == "__main__":
	insertionSortLinkedList([4,2,1,3])
	insertionSortLinkedList([2,5,1,6,10,3,99])
