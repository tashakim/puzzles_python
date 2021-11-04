# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        """
        Purpose: Return the length of the longest path in a binary tree,
        where each node in the path has the same value.

        """
        def traverse(node):
            nonlocal res
            if not node: 
                return 0

            left = traverse(node.left)
            right = traverse(node.right)
            l = r = 0

            if node.left and node.left.val == node.val:
                l = left + 1
            if node.right and node.right.val == node.val:
                r = right + 1
            res = max(res, l + r)

            return max(l, r)
        
        res = 0
        traverse(root)
        return res