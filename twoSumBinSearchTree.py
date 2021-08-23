# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root, k):
        """
        Purpose: Returns bool. indicating whether there exist two elements in a BST such that 
        their sum is equal to the given target.

        Time complexity: O(n), where n is no. of nodes in BST.
        Space complexity: O(n), same as above.
        """
        def traverse(node, cur, k):
            # Top-down recursion solution.
            if not node: return
            
            self.cache.add(node.val)
            traverse(node.left, cur, k)
            traverse(node.right, cur, k)
            
        self.cache = set()
        traverse(root, 0, set())
        for x in self.cache:
            req = k - x
            if req in self.cache and x!= req: return True
        
        return False
        

    def findTarget(self, root, k):
        """
        Purpose: Improves space complexity by searching for k - node.val == 0 (Traverses tree once).
        Time complexity: O(n), n = no. of nodes in BST,
        Space complexity: O(1).
        """
        def traverse(node, k, seen): 
            # Bottom-up recursion solution.
            if not node: return False
            
            if k-node.val in seen: return True
            seen.add(node.val)
            return traverse(node.left, k, seen) or traverse(node.right, k, seen)
        
        return traverse(root, k, set())
        