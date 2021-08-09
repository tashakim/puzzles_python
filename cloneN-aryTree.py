"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        """
        Purpose: Returns a deep-copy / clone of an n-ary tree.
        
        """
        if not root: return 
        clone = Node(val=root.val)
        
        def traverse(node, clone):
            if not node: return

            for child in node.children:
                cloned_child = Node(val=child.val)
                clone.children.append(cloned_child)
                traverse(child, cloned_child)
            
        traverse(root, clone)
        return clone