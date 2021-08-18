class Solution:
    def diameter(self, root: 'None') -> int:
        """
        Purpose: Returns the diameter (longest path found) in an n-ary tree.
        """
        self.res = 0
        def traverse(node):
            if not node:
                return 0

            subtrees = [0]
            for child in node.children:
                subtrees.append(traverse(child))

            pairs = [x for x in itertools.combinations(subtrees, 2)]
            for pair in pairs:
                self.res = max(self.res, sum(pair))
            
            return max(subtrees) + 1

        traverse(root)
        return self.res