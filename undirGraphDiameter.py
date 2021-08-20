import itertools
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        Purpose: Returns the diameter (no. of edges in longest path) in an undirected graph.
        """
        edges.sort()
        self.tree = defaultdict(lambda: [])
        for x,y in edges:
            self.tree[x].append(y)
        root = edges[0]
        self.max_path = 0
        
        def traverse(node):
            if node not in self.tree:
                return 1
            subtrees = []
            for child in self.tree[node]:
                subtrees.append(traverse(child))
            pairs = [x for x in itertools.permutations(subtrees, 2)]
        
            for x in pairs:
                self.max_path = max(self.max_path, sum(x))
            return max(subtrees) + 1 
        
        traverse(root[0])
        return self.max_path