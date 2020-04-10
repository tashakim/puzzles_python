#/usr/bin/python3


class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input given."


def numShortestPaths(g, start, end):
    """graph, start node, end node -> int
    Purpose: find the number of shortest paths between two nodes in a graph
    Raises: raise InvalidInputException if an input is None, or
    if start or end are not in g"""

    for node in [start, end]:
        # raises exception when any of the inputs are None
        if g is None or node is None:
            raise InvalidInputException("Invlaid input")
        # raises exception when start or end nodes are not in g.
        if g.containsVertex(node) == False:
        	raise InvalidInputException("Invalid input")

    for v in g.vertices():
        # sets distance of all vertices to a large value.
        v.distance = float('inf') 

    start.distance = 0 # number of nodes away from start node.
    start.paths = 1 # number of paths there are from start node.

    order = []
    order.append(start)

    while order is not None:
        # BFS
        visited = order.pop(0)

        for edge in g.incidentEdges(visited):
            adjacent = g.opposite(visited, edge)
            order.append(adjacent)
            g.removeEdge(edge)

            if(adjacent.distance > visited.distance +1):
                # updates adjacent node's distance
                adjacent.distance = visited.distance +1
                # updates adjacent node's number of paths
                adjacent.paths = visited.paths

            elif(adjacent.distance == visited.distance +1):
                adjacent.paths += visited.paths

        # when end node is visited, returns the number of paths 
        # stored in the end node.
        if(visited == end):
            return visited.paths
