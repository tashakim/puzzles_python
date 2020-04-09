class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input given."

def numShortestPaths(g, start, end):
    """graph, start node, end node -> int
    Purpose: find the number of shortest paths between two nodes in a graph
    Raises: raise InvalidInputException if an input is None, or
    if start or end are not in g"""
    vertices = []
    count = 0
    start._distance = 0
    vertices.append(start)
    shortestDist = float('inf')

    while vertices != None:
    		item = vertices.pop(0)
    		if (item != end):
    			edges = g.incidentEdges(item)
    			for edge in edges:
    				node = g.opposite(item, edge)
    				vertices.append(node)
    				node._distance = item._distance + 1
    				g.removeEdges(edge)
    		else:
    			if (item._distance < shortestDist):
    				shortestDist = item._distance
    				count = 0
    			else if (item._distance == shortestDist):
    				count += 1
    			else: 
    				return
    return count

