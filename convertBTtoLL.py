"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    """
    Purpose: Converts a binary tree into a doubly-linked list, in-place.
    """

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # In-place modification!

        def traverse(node):
            if not node: return
            traverse(node.left)
            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else: # head of linked list
                self.head = node
            self.prev = node
            traverse(node.right)
            
        if not root: return
        self.head = self.prev = None

        traverse(root)
        
        # connect the head and tail
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head


    def treeToDoublyList2(self, root: 'Node') -> 'Node':
        # Additional space O(n), n = no. of nodes in BT.
        cache = []
        def traverse(node):
            if not node: return
            traverse(node.left)
            # visit node
            cache.append(node)
            traverse(node.right)
            
        if not root: return
        traverse(root)
        
        for i in range(len(cache)):
            cache[i].right = cache[(i+1)%len(cache)]
            cache[i].left = cache[(i-1)%len(cache)]
            
        return cache[0]