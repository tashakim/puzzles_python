class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """Purpose: Returns the level order traversals of its node values,
        grouped by level.
        """
        visited = [root]
        order = []
        while visited:
            popped = visited.pop(0)
            order.append(popped.val)
            
            if popped.left:
                visited.append(popped.left)
            if popped.right:
                visited.append(popped.right)
        print(order)
        # BFs order printed.

        # print grouped by level here:
        return


if __name__ == "__main__":
    s = Solution()
    s.levelOrder([3, 9, 10, None, None, 15, 7]) 