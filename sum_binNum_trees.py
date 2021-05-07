# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def traverse(node, curPath):
            # recursively sums each root-to leaf path
            if node:
                curPath += str(node.val)
                # if leaf node is reached, 
                if node.left is None and node.right is None:
                    # append curPath to numbers.
                    numbers.append(curPath)
                traverse(node.left, curPath)
                traverse(node.right, curPath)

        numbers = []
        traverse(root, "")
        numbers = [int(n, 2) for n in numbers]
        return sum(numbers)