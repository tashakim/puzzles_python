# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        Purpose: Returns the sum of values of nodes with an even-valued grandparent, 
        of a binary tree.

        Note: If there are no nodes with an even value grandparent, returns 0.

        """
        def traverse(node):
            if not node: return
            # visit node
            if node.val % 2 == 0:
                # get node's grandchildren
                getGrandchildren(node, 0)
                
            traverse(node.left)
            traverse(node.right)
        
        self.res = 0

        def getGrandchildren(node, count):
            if not node: return
            if count == 2:
                self.res += node.val
                
            getGrandchildren(node.left, count + 1)
            getGrandchildren(node.right, count + 1)
        
        traverse(root)

        return self.res