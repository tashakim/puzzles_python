# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # DFS
        order = []
        visited = []
        visited.append(root)
        while(visited):
            popped = visited.pop()
            order.append(popped)
            if popped.left:
                visited.append(popped.left)
            if popped.right:
                visited.append(popped.right)
        nodes = [x.val for x in order]
        sum = 0
        for x in nodes:
            if x >= L and x <= R:
                sum += x
        return sum