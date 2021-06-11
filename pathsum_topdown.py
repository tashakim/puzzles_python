# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.target = targetSum
        self.bool = False
        # traverse the tree!
        # once we reach a leaf node, check if the 'sum' == target
        self.traverse(root, 0)
        return self.bool
        
        
    def traverse(self, root, curSum):
        # Purpose: Traverse the tree in postorder
        if root:
            curSum += root.val
            if root.left is None and root.right is None:
                if curSum == self.target:
                    self.bool = True
            self.traverse(root.left, curSum)
            self.traverse(root.right, curSum)
        