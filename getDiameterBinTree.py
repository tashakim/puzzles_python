# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Purpose: Recursively calculates the diameter (longest path) found in given binary tree.

        """
        def traverse(node): 
            if not node: 
                return 0

            left_subtree = traverse(node.left)
            right_subtree = traverse(node.right)

            self.max_sum = max(left_subtree + right_subtree, self.max_sum)
            
            return max(left_subtree, right_subtree) + 1

        self.max_sum = float('-inf')
        traverse(root)

        return self.max_sum