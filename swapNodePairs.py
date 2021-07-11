def swapNodePairs(head: ListNode) -> ListNode:
    # Purpose: Swaps nodes in a linked list, in pairs.
    
    if not head or head.next:
        return head
    first = node
    second = node.next

    first.next = swapNodePairs(second.next)
    second.next = first

    return second