# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

<<<<<<< HEAD
class Solution:
=======
class DepthMethods:
    """Purpose: This class contains recursive methods related to the depth or
    height of a binary tree. E.g. max and min depth / heights.
    """
>>>>>>> f8a7ea8b52ff8807ba378e2249b6f8c35f697ff7
    def maxDepth(self, root: TreeNode) -> int:
        # Time complexity: O(n)
        # Space complexity: O(n) worst case - if tree is completely unbalanced
            # O(log(n)) best case - tree is completely balanced
        def bst(root):
            if not root:
                return 0
            left_subtree_depth = bst(root.left)
            right_subtree_depth = bst(root.right)
            
            return max(left_subtree_depth, right_subtree_depth) + 1
        return bst(root)

<<<<<<< HEAD
class Solution:
=======
>>>>>>> f8a7ea8b52ff8807ba378e2249b6f8c35f697ff7
    def minDepth(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == 0 or right == 0:
                return max(left, right) + 1
            return min(left,right) + 1

        return dfs(root) 

<<<<<<< HEAD
class Solution:
=======
class TreeShape:
    """Purpose: This class contains recursive methods related to the shape of 
    the binary tree. E.g. balanced, complete, symmetric etc.
    """
>>>>>>> f8a7ea8b52ff8807ba378e2249b6f8c35f697ff7
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
<<<<<<< HEAD
    def height(self, node):
=======
    def height_helper(self, node):
        """Purpose: This is a helper method used in the isBlanced method, 
        to retrieve the height of a binary tree.
        """
>>>>>>> f8a7ea8b52ff8807ba378e2249b6f8c35f697ff7
        if not node:
            return 0
        left_subtree_height = self.height(node.left)
        right_subtree_height = self.height(node.right)
        return max(left_subtree_height, right_subtree_height) + 1

<<<<<<< HEAD
class Solution:
=======
>>>>>>> f8a7ea8b52ff8807ba378e2249b6f8c35f697ff7
    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right:
                 return True
            if not left or not right:
                  return False

            if left.val == right.val:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
            return False
        
        if not root:
            return True
<<<<<<< HEAD
        return dfs(root.left, root.right)
=======
        return dfs(root.left, root.right)

class Other:
    def lowestCommonAncestor(self, root, p, q):
        """Purpose: Returns the lowest common ancestor node aka - the 'splitting' node.
        """
        # If both p and q are greater than parent
        if p.val > root.val and q.val > root.val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p.val < root.val and q.val < root.val:    
            return self.lowestCommonAncestor(root.left, p, q)
        
        # We have found the lowest-common point, i.e. the 'splitting' node.
        return root

>>>>>>> f8a7ea8b52ff8807ba378e2249b6f8c35f697ff7
