# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_length = 1
        cur_length = 1
        
        def traverse(node, parent, cur_length):
            # Purpose: traverses a binary tree recursively
            if node:
                # visit node
                if parent and parent.val + 1 == node.val:
                    cur_length += 1
                else:
                    cur_length = 1
                self.max_length = max(cur_length, self.max_length)
                traverse(node.left, node, cur_length)
                traverse(node.right, node, cur_length)
        
        traverse(root, None, cur_length)
        return self.max_length