def swapNodePairs(head: ListNode) -> ListNode:
    # Purpose: Recursively swaps nodes in a linked list, in pairs.

    if not head or head.next:
        return head
    first = node
    second = node.next

    first.next = swapNodePairs(second.next)
    second.next = first

    return second


def swapNodePairs(head: ListNode) -> ListNode:
    # Purpose: Iteratively swaps nodes in a linked list, in pairs.
    
    dummy = ListNode(-1)
    dummy.next = head
    dummy = prev

    while head and head.next:
        first = head
        second = head.next

        prev.next, first.next, second.next = second, second.next, first

        prev = first
        head = first.next

    return dummy.next