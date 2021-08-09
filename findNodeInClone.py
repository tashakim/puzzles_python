# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        """
        Purpose: Returns a ference to a node `target` in the original tree, 
        given two binary trees `original` and `cloned`.

        Note: The cloned tree is a copy of the original tree.
        Returns a reference to the same node in the CLONED tree.
        """
        def traverse(original, cloned):
            """
            Purpose: Traverses both trees at once via depth-first search.
            
            """
            if not original or not cloned: 
                return
            # visit node
            if original == target: 
                self.res = cloned
                return cloned
            traverse(original.left, cloned.left)
            traverse(original.right, cloned.right)

        self.res = TreeNode()
        traverse(original, cloned)
        
        return self.res
