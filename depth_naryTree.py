"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0
        depth = 1
        def traverse(node, depth):
            if node:
                self.max_depth = max(depth, self.max_depth)
                # recursively call on each child
                for child in node.children:
                    traverse(child, depth + 1)
                    
        # call function
        traverse(root, depth)
        return self.max_depth
            