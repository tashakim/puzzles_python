# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.lonely = []
        self.traverse(root, self.lonely)
        return self.lonely
        
        
    def traverse(self, node, lonely_nodes):
        if node:    
            # visit node
            # if either left or right node doesn't exist:
            if (node.left is None and node.right):
                lonely_nodes.append(node.right.val)
            if (node.right is None and node.left):
                # add that child node value to lonely_nodes
                lonely_nodes.append(node.left.val)
                
            self.traverse(node.left, lonely_nodes)
            self.traverse(node.right, lonely_nodes)
            