# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	"""Purpose: Recursively returns the maximum depth of 
	any node in a n-ary tree.
	"""
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = 0
        
        for node in [root.left, root.right]:
            depth = max(depth, self.maxDepth(node))
        
        return depth +1