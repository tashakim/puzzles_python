class Solution:
    def countComponents(self, n, edges):
        """
        Purpose: Returns the no. of connected components in given graph.

        Depth-first search solution.
        """
        graph = [[] for x in range(n)]
        visited = [False for x in range(n)]

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def traverse(node):
            for x in node:
                if not visited[x]:
                    visited[x] = True
                    traverse(x)

        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                count += 1
                traverse(i)
        
        return count