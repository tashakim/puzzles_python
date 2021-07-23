class Solution:
    def canComplete(self, numCourses: int, prereqs: List[int]):
        """
        Purpose: Traverses adjacency graph representing course and its prerequisites, and returns whether 
        it is possible to complete all courses by taking at most numCourses no. of courses.
        """
        visited = [0 for x in range(numCourses)]
        graph = [[] for x in range(numCourses)]

        # First, construct adjacency graph
        for x,y in prereqs:
            graph[x].append(y)

        def traverse(i):
            if visited[i] == 1: return False
            if visited[i] == 2: return True

            visited[i] = 1
            for neighbor in visited[i]:
                if not traverse(neighbor):
                    return False
            visited[i] = 2
            return True

        for i in range(numCourses):
            if not traverse(i):
                return False

        return True