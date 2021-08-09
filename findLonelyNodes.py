# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        """
        Purpose: Given root of a bin. tree, returns an array containing values of all
        lonely nodes in the tree.
        
        Note: The array can be returned in any order.
        
        """
        def traverse(node):
            if not node: return
            
            # visit node
            if (node.left and not node.right):
                self.res.append(node.left.val)
            if (not node.left and node.right):
                self.res.append(node.right.val)
                
            traverse(node.left)
            traverse(node.right)
            
        self.res = []
        traverse(root)
        return self.res