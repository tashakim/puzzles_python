from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Purpose: Recursively appends once entire tree is traversed in depth-first search way.
        """
        if not root: return []
        self.order = []
        self.maxDepth = 0
        depth = 0
        
        def traverse(node, depth):
            if node:
                if node.left or node.right:
                    self.order.append([])
                self.maxDepth = max(depth, self.maxDepth)
                if node.left:
                    self.order[depth].append(node.left.val)
                    traverse(node.left, depth + 1)
                if node.right:
                    self.order[depth].append(node.right.val)
                    traverse(node.right, depth + 1)
        traverse(root, depth)    
        self.order.insert(0, [root.val])
        return self.order[:self.maxDepth + 1]
                
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Purpose: Iteratively appends to order in a breadth-first search way.
        """
        if not root: return []

        order = []
        visited = [root]
        while visited:
            cur_level, next_level = [], []
            for node in visited:
                cur_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            order.append(cur_level)
            visited = next_level

        return order