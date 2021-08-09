# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Purpose: Checks whether two binary trees are equivalent or not,
        given roots `p`, `q` of two binary trees.

        Note: Two bin. trees are equivalent if they are structurally identical, and 
        nodes have the same value.
        """
        def traverse(node1, node2): # method 1
            # Use global bool. to keep track of equivalency.
            if (node1 and not node2) or (not node1 and node2): 
                self.bool = False
                return 

            if not node1 and not node2: return 
            # visit node
            if node1.val != node2.val:
                self.bool = False

            traverse(node1.left, node2.left)
            traverse(node1.right, node2.right)
        
        self.bool = True
        
        traverse(p, q)
        return self.bool


    def isSameTree(self, p, q): # method 2
        def traverse(node1, node2):
            # Uses bottom-up approach.
            if (node1 and not node2) or (not node1 and node2): 
                return False
            if not node1 and not node2: return True
            # visit node
            if node1.val != node2.val:
                return False
            return traverse(node1.left, node2.left) and traverse(node1.right, node2.right)
        
        return traverse(p, q)


    def isSameTree(self, p, q): # method 3
        def traverse(root, order):
            if not root or root == []: return []
            if root: 
                order.append(root.val)
                
            if root.left:    
                traverse(root.left, order)
            else: 
                order.append("null")
            if root.right:
                traverse(root.right, order)
            else: 
                order.append("null")
                
            return order

        return traverse(p, []) == traverse(q, [])