from heappriorityqueue import *
from mygraph import *

def dijkstra(g, src):
    """ Calculate the shortest path tree from the src in the input
    connected graph g using Dijkstra's algorithm. The elements attached
    to the edges should be the distances. Must run in O((|E| + |V|) log |V|)
    time using the provided HeapPriorityQueue data structure.

    Returns the shortest path tree in the form of a new MyGraph object.
    Do not modify the input MyGraph instance.

    Raise the InvalidInputException if input is None or if src is not in g.

    Note: To access the actual vertices in the HeapPriorityQueue,
    you need to call pop().value(), not just pop().
    """
    if g is None or src is None:
        raise InvalidInputException("Error: Invalid input")
    if src not in g.vertices():
        raise InvalidInputException("Error: Invalid src node")

    for v in g.vertices():
        # sets distance of all vertices to a very large value.
        v.distance = float('inf')
        v.prev = None
    src.distance = 0
    dist = []
    MST = []

    for v in g.vertices():
        dist.append(v.distance)

    Q = HeapPriorityQueue()
    for v in g.vertices():
        v.entry = Q.push(v.distance, v)
        print("v.entry is:", v.entry)
    print("Q is: ", Q)
    print("MST: ", MST)
    while Q.isEmpty() != True:
        u = Q.pop().value()
        for edge in g.incidentEdges(u):
            v = g.opposite(u, edge)
            if(v.distance > u.distance + g.connectingEdge(u,v).element()):
                #updates adjacent node's distance
                v.distance = u.distance +g.connectingEdge(u,v).element()
                MST.append(edge)
                v.prev = u
                Q.replaceKey(v.entry, v.distance)
    print("edges are: ",g.edges())
    print("Q is: ", Q)
    print("MST is: ", MST)
    ret_g = MyGraph()
    for v in g.vertices():
        ret_g.insertVertex(v)
    """for e in MST:
                    ret_g.insertEdge(e)"""
    return ret_g


class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input Given."
