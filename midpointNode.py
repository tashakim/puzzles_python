# Can you find the middle node of a linked list? 
# If there are 2 middle nodes, return the second one.
def findMidpoint(head): # first middle? try this
	dummy = ListNode(0, head)
	ptr1, ptr2 = dummy, dummy
	while ptr1 and ptr1.next:
		ptr1 = ptr1.next.next
		ptr2 = ptr2.next 

	if ptr1: ptr2 = ptr2.next # even no. of nodes, return the second one

	return ptr2


def findMidpoint(head):
	ptr1 = ptr2 = head
	while ptr1 and ptr1.next:
		ptr1 = ptr1.next.next
		ptr2 = ptr2.next
	return ptr2


def findMidpoint(head):
	# S: O(n), n is length of list
	storage = []
	# Using some extra space
	cur = head
	length_of_list = 0
	while cur:
		length_of_list += 1 # count length of list simultaneously
		storage.append(cur.val)
		cur = cur.next
	return storage[len(storage) // 2]
