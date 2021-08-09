# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        Purpose: Returns the sum of all 'left leaves' of a binary tree.
        
        """
        def traverse(node):
            if not node: return
            
            # visit node
            if node.left and not node.left.left and not node.left.right:
                print(node.left.val)
                self.res += node.left.val
                
            traverse(node.left)
            traverse(node.right)
        
        self.res = 0
        traverse(root)
        return self.res