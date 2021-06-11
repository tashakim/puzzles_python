# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def traverse(node):
            if node:
                # if leaf node found, add to sequence
                if not node.left and not node.right:
                    sequence.append(node.val)
                else:
                    traverse(node.left)
                    traverse(node.right)
        sequence = []
        traverse(root1)
        first_sequence = sequence
        sequence = []
        traverse(root2)
        return first_sequence == sequence
        