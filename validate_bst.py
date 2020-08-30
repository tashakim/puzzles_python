# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, low = float('-inf'), high = float('inf')):
            if not root: return True
            
            if root.val <= low or root.val >= high:
                return False
            
            if not helper(root.left, low, root.val):
                return False
            if not helper(root.right, root.val, high):
                return False
            return True
        
        return helper(root)


    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, low = float('-inf'), high = float('inf')):
            if not root: 
                return True
            
            if root.val <= low or root.val >= high: # BST condition
                return False
            
            if not helper(root.left, low, root.val):
                return False
            if not helper(root.right, root.val, high):
                return False
            
            return True
        
        return helper(root)


    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(root, low, high):
            if not root:
                return True
            val = root.val
            if val > low and val < high and isValid(root.left, low, root.val) and isValid(root.right, root.val, high):
                return True
            return False
        
        return isValid(root, float('-inf'), float('inf'))
        
            