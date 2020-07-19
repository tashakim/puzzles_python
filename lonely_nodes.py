# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        # BFS
        visited = [root]
        order = []
        
        while visited:
            popped = visited.pop()
            # decorate popped node
            order.append(popped)
            if popped.left:
                visited.append(popped.left)
            if popped.right:
                visited.append(popped.right)
            
        l = []
        for item in order:
            if self.hasLeft(item) and not self.hasRight(item):
                l.append(item.left.val)
            elif self.hasRight(item) and not self.hasLeft(item):
                l.append(item.right.val)
        return l
        # if node has only one child (left or right), it is a lonely node.
        
    def hasLeft(self, node):
        return node.left != None
    
    def hasRight(self, node):
        return node.right != None