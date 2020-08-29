# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    """Purpose: Searches binary tree for input value.
    If value does not exist, return empty list.

    Time complexity:
    Space complexity:
    """
        visited, order = [root], []
        while visited:
            popped = visited.pop(0)
            # decorate popped node            
            if popped.val == val:
                return popped
            if popped.left:
                visited.append(popped.left)
            if popped.right:
                visited.append(popped.right)
                