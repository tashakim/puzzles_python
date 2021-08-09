"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import defaultdict
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        Purpose: Returns the level-order traversal of an n-ary tree nodes' values.

        """
        self.d = defaultdict(lambda: [])

        def traverse(node, depth):
            if not node: return
            # visit node
            self.d[depth].append(node.val)
            for child in node.children:
                traverse(child, depth+1)
        
        if not root: return
        traverse(root, 0)
        
        res = [[] for i in range(len(self.d))]
        for k,v in self.d.items():res[k] = v
            
        return res