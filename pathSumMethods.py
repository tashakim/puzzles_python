####################################################################
# Variations of path sum
####################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
####################################################################

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        Purpose: Returns a boolean indicating whether a binary tree has a 
        root-to-leaf path such that all values along the path add to `targetSum`.
        
        """
        def traverse(node, cur_sum):
            if not node:
                return
            
            # visit node
            if not node.left and not node.right:
                if cur_sum - node.val == 0:
                    self.bool = True
                return
            
            if node.left:
                traverse(node.left, cur_sum - node.val)
            if node.right:
                traverse(node.right, cur_sum - node.val)
                
        self.bool = False
        if not root: return
        traverse(root, targetSum)

        return self.bool


    def pathSumII(self, root, targetSum):
        """
        Purpose: Returns a list of all root-to-leaf paths such that all values 
        along the path add to `targetSum`.

        """
        def traverse(node, cur_sum, path):
            if not node: return

            if not node.left and not node.right:
                if cur_sum == node.val:
                    path.append(node.val)
                    self.res.append(path)
                
            traverse(node.left, cur_sum - node.val, path + [node.val])
            traverse(node.right, cur_sum - node.val, path + [node.val])

        self.res = []
        traverse(root, targetSum, [])

        return self.res
        

    def pathSumIII(self, root: TreeNode, targetSum: int) -> int:
        """
        Purpose: Returns the number of paths where the sum of values along each path 
        equals `targetSum`. 

        Note the paths do not have to be root-to-leaf, instead must go downwards.

        """
        def traverse(node):
            """
            Purpose: Traverses binary tree in depth-first-search way.
            """
            if not node: return
            # visit node
            findPaths(node, targetSum)
            
            traverse(node.left)
            traverse(node.right)
                
        def findPaths(node, cur_sum):
            """
            Purpose: Counts the number of paths (not necessary root-to-leaf), where 
            path values sum to targetSum value.
            """
            if not node: return
            if cur_sum - node.val == 0:
                self.count += 1
                
            findPaths(node.left, cur_sum - node.val)
            findPaths(node.right, cur_sum - node.val)
                
        self.count = 0
        traverse(root)

        return self.count