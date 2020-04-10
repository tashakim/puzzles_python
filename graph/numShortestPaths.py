import numShortestPaths
from importlib import reload
reload(numShortestPaths)
from numShortestPaths import *
from mygraph import *
import pytest

class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input given."

def numShortestPaths(g, start, end):
    """graph, start node, end node -> int
    Purpose: find the number of shortest paths between two nodes in a graph
    Raises: raise InvalidInputException if an input is None, or
    if start or end are not in g"""
    if g.containsVertex(start) == False or g.containsVertex(end) == False:
    	raise InvalidInputException("Invalid input")

    if g is None or start is None or end is None:
    	raise InvalidInputException("Invlaid input")

    for v in g.vertices():
        v.distance = float('inf')

    start.distance = 0
    start.paths = 1
    order = []
    order.append(start)

    while order is not None:
        visited = order.pop(0)
        for edge in g.incidentEdges(visited):
            adjacent = g.opposite(visited, edge)
            order.append(adjacent)
            g.removeEdge(edge)
            if(adjacent.distance > visited.distance +1):
                adjacent.distance = visited.distance +1
                adjacent.paths = visited.paths
            elif(adjacent.distance == visited.distance +1):
                adjacent.paths += visited.paths
            return 1
        if(visited == end):
            return end.paths