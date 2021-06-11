# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, node: TreeNode) -> int:
        self.count = 0
        def traverse(node):
            # 
            if not node: return True
            left_subtree = traverse(node.left)
            right_subtree = traverse(node.right)
            if left_subtree and right_subtree and (not node.left or node.left.val == node.val) and (not node.right or node.right.val == node.val):
                self.count += 1
                return True
            return False
            
        traverse(node)
        return self.count