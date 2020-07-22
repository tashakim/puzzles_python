def hasCycle(self, head: ListNode) -> bool:
	"""Purpose: Simple implementation of Floyd's 
	cycle detection algorithm.
	Space Complexity: O(1),
	Time Complexity: O(n).
	"""
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next # increment by one
            fast = fast.next.next # increment by two
            if slow == fast:
                return True # cycle detected!
        return False # no cycles detected

def hasCycle1(self, head: ListNode) -> bool:
	"""Purpose: A slightly slower solution involving
	writing to a node's data, to indicate it has been
	visited. 
	Once we come across a node that has been visited 
	before, we return True.
	Space Complexity: O(1),
	Time Complexity: O(n).
	"""
        node = head
        while node:
            if node.val == float('-inf'):
                return True
            node.val = float('-inf')
            node = node.next
        return False