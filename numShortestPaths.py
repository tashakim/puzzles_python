class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input given."

def numShortestPaths(g, start, end):
    """graph, start node, end node -> int
    Purpose: find the number of shortest paths between two nodes in a graph
    Raises: raise InvalidInputException if an input is None, or
    if start or end are not in g"""
    dist = [float('inf')] * end 
    paths = [0] * end
    BFS(g, start, dist, paths, end) 
    print("Numbers of shortest Paths are:", end=" ") 
    for i in paths: 
        print(i, end=" ")  

def BFS(adj: list, src: int, dist: list, paths: list, n: int): 
    visited = [False] * n 
    dist[src] = 0
    paths[src] = 1
  
    q = deque() 
    q.append(src) 
    visited[src] = True
    while q: 
        curr = q[0] 
        q.popleft() 
  
        # For all neighbors of current vertex do: 
        for x in adj[curr]: 
  
            # if the current vertex is not yet 
            # visited, then push it to the queue. 
            if not visited[x]: 
                q.append(x) 
                visited[x] = True
  
            # check if there is a better path. 
            if dist[x] > dist[curr] + 1: 
                dist[x] = dist[curr] + 1
                paths[x] = paths[curr] 
  
            # additional shortest paths found 
            elif dist[x] == dist[curr] + 1: 
                paths[x] += paths[curr] 
  