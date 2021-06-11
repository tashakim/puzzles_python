# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def traverse(node, curPath):
            if node:
                curPath += str(node.val)

                if node.left is None and node.right is None:           
                    res.append(curPath)
                else:
                    curPath += "->"
                    traverse(node.left, curPath)
                    traverse(node.right, curPath)
        res = []
        traverse(root, "")
        return res
        
    
    """
    def binaryTreePaths(self, root):
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths  
                else:
                    path += '->'  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)
        paths = []
        construct_paths(root, '')
        return paths
    """