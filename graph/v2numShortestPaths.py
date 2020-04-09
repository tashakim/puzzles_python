import numShortestPaths
from importlib import reload

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

    vertices = []
    count = 1
    start.distance = 0
    vertices.append(start)
    #print("size of vertices is: ", len(vertices))
    shortestDist = float('inf')

    while len(vertices) != 0:
    		item = vertices.pop(0)
    		if (item != end):
    			if g.incidentEdges(item) != None:
	    			for edge in g.incidentEdges(item):
	    				node = g.opposite(item, edge)
	    				vertices.append(node)
	    				node.distance = item.distance + 1

	    				g.removeEdge(edge)
	    	else:			
	    				if(item.distance < shortestDist):
	    					shortestDist = item.distance
	    					count =1
	    				elif(item.distance == shortestDist):
	    					count +=1
	    				
    return count
