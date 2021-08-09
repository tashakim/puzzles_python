# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        Purpose: Returns the sum of values of a bin. tree deepest leaves.

        """
        def traverse(node, depth):
            """
            Purpose: Traverses binary tree in depth-first search way.
            """
            if not node: return
            # visit node
            if not node.left and not node.right:    
                if node.val in self.res:
                    self.res[node.val] = max(depth, self.res[node.val])
                else: 
                    self.res[node.val] = depth

                return
            
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)
            
        self.res = {}
        traverse(root, 1)

        res = 0
        max_val = max(self.res.values())
        for k, v in self.res.items():
            if v == max_val:
                res += k

        return res