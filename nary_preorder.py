"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        order = []
        my_stack = [root]
        while my_stack:
            popped = my_stack.pop()
            if popped:
                order.append(popped.val)
                for child in reversed(popped.children):
                    my_stack.append(child)
                
        return order