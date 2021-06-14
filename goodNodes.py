# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Purposse: Returns how many good nodes there are in a binary tree.
        A node Z is 'good' if in the path from root to Z there are no nodes with a value
        greater than Z.
        Example: [2, None, 4, 10, 8, None, None, 4] -> 4
        """
        self.count = 1
        def traverse(node, mymax):
            if not node: return None
            # visit node
            mymax = max(node.val, mymax)
            if node.left:
                if node.left.val >= mymax:
                    self.count += 1
                traverse(node.left, mymax)
            if node.right:
                if node.right.val >= mymax:
                    self.count += 1
                traverse(node.right, mymax)
        traverse(root, root.val)
        
        return self.count 