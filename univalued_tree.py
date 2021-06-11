# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.univ = root.val
        self.bool = True
        def traverse(node):
            if node:
                if node.val != self.univ:
                    self.bool = False
                else:
                    traverse(node.left)
                    traverse(node.right)
            
        traverse(root)
        return self.bool