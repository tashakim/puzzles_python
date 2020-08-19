class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		

class Solution:
	def oddEvenList(self, head: ListNode) -> ListNode:
		"""Purpose: Given a singly linked list, groups all nodes positioned at 
		odd indices together, followed by those at even indices.
		"""
		if not head:
			return None
		
		odd = head
		even_head = even = head.next
		
		while even and even.next:
			odd.next = odd.next.next
			even.next = even.next.next
			
			odd = odd.next
			even = even.next
			
		odd.next = even_head
	
		return head