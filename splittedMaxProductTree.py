# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Purpose: Returns the max. product of sums of the subtrees, resulting from splitting a binary 
        tree into two subtrees by removing one edge.

        """
        self.res_array = []
        self.tot_sum = 0
        
        def traverse(node):
            if not node: 
                return 0
            
            left_subtree = traverse(node.left)
            right_subtree = traverse(node.right)
            self.tot_sum += node.val
            cur_val = node.val + left_subtree + right_subtree
            self.res_array.append(cur_val)
            
            return left_subtree + right_subtree + node.val

        max_prod = float('-inf')
        traverse(root)
        for i, x in enumerate(self.res_array):
            max_prod = max(max_prod, x * (self.tot_sum - x))

        return max_prod % (10**9 + 7)