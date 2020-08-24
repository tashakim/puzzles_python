# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
    """Purpose: Computes the length of the diameter (longest path) 
    in a binary tree. The path can pass through the root.
    """
        self.max_len = 0
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.max_len = max(self.max_len, l+r)

            return max(l,r) +1
            
        dfs(root)
        return self.max_len