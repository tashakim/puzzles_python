""" Topological Sort

"""
from mydigraph import *


def topological_sort(dag):
    """topological_sort: dag -> list of vertices
    Purpose: Runs a topological sort on a DAG
    Consumes: a directed acyclic graph
    Produces: a list of topologically sorted vertices, or empty list if graph is empty
    Raises: A GraphCycleException if no topological sorting
        is possible on the input DAG
    An InvalidInputException if the graph is None.
    Example:                    A -\
             topological_sort(      C -> D ) -> [A, B, C, D]
                                B -/
    """
    # raises exception when any of the inputs are None
    if dag is None:
        raise InvalidInputException("Invalid input")

    d = {} # dictionary to store node and its distance
    s = [] # stack
    l = [] # list

    for v in dag.vertices():
        d[v] = len(dag.incidentEdges(v))

    for key,value in d.items():
        if(value == 0):
            s.append(key)

    while s != []:
        visited = s.pop()
        l.append(visited)

        for e in dag.emanantEdges(visited):
            w = dag.opposite(visited, e)
            d[w] -= 1

            dag.removeEdge(e)
            if(0 in d.values()):
                if(d.get(w) == 0):
                    s.append(w)

    # Raises Exception when the DAG is not acyclic.
    if any(x != 0 for x in d.values()):
        raise GraphCycleException()    
    # returns list of vertices in sorted order
    return l


class GraphCycleException(Exception):
    def __str__(self):
        return "Topological sort failed. A cycle occured."


class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input Given."
