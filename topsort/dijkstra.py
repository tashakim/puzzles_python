from heappriorityqueue import *
from mygraph import *


def dijkstra(g, src):
    """ Purpose:Calculate the shortest path tree from the src in the input
    connected graph g using Dijkstra's algorithm. The elements attached
    to the edges should be the distances. Must run in O((|E| + |V|) log |V|)
    time using the provided HeapPriorityQueue data structure.

    Output: Returns the shortest path tree in the form of a new MyGraph object.
    Do not modify the input MyGraph instance.
    Exception: Raise the InvalidInputException if input is None or if src is not in g.
    """
    # raises Exception when graph or source node are null.
    if g is None or src is None:
        raise InvalidInputException("Error: Invalid input")
    # raises Exception when the source node is not part of input graph.
    if src not in g.vertices():
        raise InvalidInputException("Error: Invalid src node")


    for v in g.vertices():
        # initialize distances of all nodes as infinite.
        v.distance = float('inf') 
        v.prev = None
        v.visited = False
    # initialize source node's distance to 0.
    src.distance = 0 

    # Creates an empty heap-priority queue.
    Q = HeapPriorityQueue() 
    for v in g.vertices():
        v.entry = Q.push(v.distance, v)

    while Q.isEmpty()!=True:
        # pop the node with smallest priority(distance).
        u = Q.pop().value() 
        neighbor = []

        for v in g.vertices():
            if(g.areAdjacent(u,v) and v.visited == False):
                neighbor.append(v)

        for v in neighbor:
            # update distance and previous node of v.
            if(v.distance > u.distance + g.connectingEdge(u,v).element()):
                v.distance = u.distance + g.connectingEdge(u,v).element()
                v.prev = u 
                # replace v's key in the priority queue.
                Q.replaceKey(v.entry, v.distance)
                u.visited = True


    # Create a new MyGraph object to return.
    tree = MyGraph() 
    x= g.iterVertices() 

    # iterable vertices, runs in O(1).
    for i in range(g.numVertices()):
        # insert all vertices and new edges into output graph.
        node = next(x)
        tree.insertVertex(node)

    x = g.iterVertices()
    for i in range(g.numVertices()):
        node = next(x)

        # if previous node is in graph, add an edge.
        if(node.prev is not None): 
            tree.insertEdge(node, node.prev, g.connectingEdge(node, node.prev))

    # returns the MST of input graph g.
    return tree


class CyclicGraphOutputException(Exception):
    def __str__(self):
        return "Invalid output given."

class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input Given."
