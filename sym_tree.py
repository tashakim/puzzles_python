# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # if root doesn't exist, return True
        if not root:
            return True
        
        # call recurse() on left & right children
        return self.recurse(root.left, root.right)
        
        
    def recurse(self, left, right):
        print(left, right)
        # Purpose: Sets self.bool to False if tree is not symmetric.
        if left is None and right is None:
            return True
        # cases where tree is not symmetric:
            # (1) ONLY left child exists, (2) ONLY right child exists, (3) 
        if left is None:
            return False
        if right is None:
            return False
        if left.val != right.val:
            return False
        
        return (self.recurse(left.right, right.left) and self.recurse(left.left, right.right))
     