"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.order = []
        def traverse(node):
            if node:
                for child in node.children:
                    traverse(child)
                # visit node
                self.order.append(node.val)
                
        traverse(root)
        return self.order