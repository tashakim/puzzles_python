# %% [markdown]
# # Task3.1 Finish DoublyLinkedList


class DoublyLinkedList:
    """
    A linked list container built on `ListNode`. Two pseudo nodes are used for
    head and tail.
    """

    def __init__(self):
        self.head = ListNode(None)  # pseudo-node
        self.tail = ListNode(None)  # pseudo-node
        self.head.next = self.tail
        self.tail.prev = self.head
        self._length = 0

    def __len__(self):
        return self._length

    def get_last(self):
        """ Returns the last node (psedu-node is skipped). 
        Raises IndexError when no node exists. """
        if self._length == 0:
            raise IndexError("Try to get item from an empty LinkedList")
        return self.tail.prev

    def prepend(self, node):
        """
        Insert `node` at the head of the linked list
        """  
        next_node = self.head.next
        next_node.prev = node
        node.next = next_node
        self.head.next = node
        node.prev = self.head
        self._length += 1
        

    def remove(self, node):
        """
        Remove `node` from this linked list
        """  
        new_node = node.prev
        temp = node.next
        new_node.next = temp
        temp.prev = new_node
        self._length -= 1
        

    def __str__(self):
        return str(self.head)
        
    class HasLoopException(Exception):
        pass
    
# %%
class ListNode:
    '''Doubly linked list node.'''
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.data = val
        
    def __str__(self):
        """ Return string representation of data in this node and all successor nodes """
        node = self
        visited = set()
        first = True
        result = ''

        while node:
            if first:
                first = False
            else:
                result += ' -> '
            if id(node) in visited:
                if node.next is not node:
                    result += str(node.data)
                    result += ' -> ... -> '
                result += str(node.data)
                result += ' -> ...'
                break
            else:
                result += str(node.data)
                visited.add(id(node))
            node = node.next
        return result


# %%
if __name__ == "__main__":
    # Examples for DoublyLinkedList
    dll = DoublyLinkedList()
    node1 = ListNode((1,1))
    node2 = ListNode((2,2))
    node3 = ListNode((3,3))

    # Prepend nodes
    dll.prepend(node1)
    dll.prepend(node2)
    print(dll)
    print("Head: ", dll.head)
    dll.prepend(node3)
    print(dll)
    
    # Remove nodes
    dll.remove(node1)
    print(dll)
    dll.remove(node3)
    print(dll)
    dll.remove(node2)
    print(dll)

