#/usr/bin/python3


# DO NOT DELETE THESE STATEMENTS
import numShortestPaths
from importlib import reload
reload(numShortestPaths)
from numShortestPaths import *
from mygraph import *
import pytest


# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.

# DO NOT write your tests within the example test functions we provide!
# Our scripts will skip the test functions we provide, so write your own
# functions to test your code thoroughly.

# Here are some example test functions.


def sample_test():
    """This method is a sample test that checks correct 
    outputs are given using this program.
    """
    assert True != False, 'Error: True is equal to False'


def test1():
    """This method is an example test that checks outputs of 
    numShortestPaths.py for a graph with three vertices.
    """
    g = MyGraph()
    v0 = GraphVertex("v0")
    v1 = GraphVertex("v1")
    v2 = GraphVertex("v2")
    g.insertVertex(v0)
    g.insertVertex(v1)
    g.insertVertex(v2)

    e0 = GraphEdge("e0", 1)
    e1 = GraphEdge("e1", 1)
    e2 = GraphEdge("e2", 1)

    g.insertEdge(v0, v2, e0)
    g.insertEdge(v0, v1, e1)
    g.insertEdge(v1, v2, e2)

    ret = numShortestPaths(g, v0, v2)
    assert ret == 1


def singlePathTest():
    """This method checks that the algorithm returns the 
    correct number of shortest path, which is 1, for a 
    graph with only two nodes, start and end.
    """
    g = MyGraph()
    v0 = GraphVertex("start")
    v1 = GraphVertex("end")

    g.insertVertex(v0)
    g.insertVertex(v1)
    
    e0 = GraphEdge("single_edge", 1)
    g.insertEdge(v0, v1, e0)

    assert numShortestPaths(g, v0, v1) == 1, "single-path test failed."


def multiplePathsTest():
    """This method checks that the algorithm returns 
    the correct number of shortest paths, when there 
    are more than one way of reaching the end node.
    """
    g = MyGraph()
    v0 = GraphVertex("v0")
    v1 = GraphVertex("v1")
    v2 = GraphVertex("v2")
    v3 = GraphVertex("v3")

    g.insertVertex(v0)
    g.insertVertex(v1)
    g.insertVertex(v2)
    g.insertVertex(v3)

    e0 = GraphEdge("e0", 1)
    e1 = GraphEdge("e1", 1)
    e2 = GraphEdge("e2", 1)
    e3 = GraphEdge("e3", 1)

    g.insertEdge(v0, v3, e0)
    g.insertEdge(v0, v1, e1)
    g.insertEdge(v1, v2, e2)
    g.insertEdge(v3, v2, e3)
    ret = numShortestPaths(g, v0, v2)

    assert ret == 2


def complicatedPathsTest():
    """This method checks that the algorithm returns
    the correct number of shortest paths in the graph, when
    there are numerous complicated paths reaching the end 
    node, as well as paths that don't lead to the end node.
    """
    g = MyGraph()
    start = GraphVertex("start")
    A = GraphVertex("A")
    B = GraphVertex("B")
    C = GraphVertex("C")
    D = GraphVertex("D")
    E = GraphVertex("E")
    F = GraphVertex("F")
    G = GraphVertex("G")
    H = GraphVertex("H")
    end = GraphVertex("end")
    g.insertVertex(start)
    g.insertVertex(A)
    g.insertVertex(B)
    g.insertVertex(C)
    g.insertVertex(D)
    g.insertVertex(E)
    g.insertVertex(F)
    g.insertVertex(G)
    g.insertVertex(H)
    g.insertVertex(end)

    e0 = GraphEdge("e0", 1)
    e1 = GraphEdge("e1", 1)
    e2 = GraphEdge("e2", 1)
    e3 = GraphEdge("e3", 1)
    e4 = GraphEdge("e4", 1)
    e5 = GraphEdge("e5", 1)
    e6 = GraphEdge("e6", 1)
    e7 = GraphEdge("e7", 1)
    e8 = GraphEdge("e8", 1)
    e9 = GraphEdge("e9", 1)
    e10 = GraphEdge("e10", 1)

    g.insertEdge(start, A, e0)
    g.insertEdge(start, B, e1)
    g.insertEdge(start, C, e2)
    g.insertEdge(A,D,e3)
    g.insertEdge(D,H,e4)
    g.insertEdge(D,G,e5)
    g.insertEdge(B,E,e6)
    g.insertEdge(B,F,e7)
    g.insertEdge(G,end,e8)
    g.insertEdge(E, end, e9)
    g.insertEdge(F, end, e10)

    ret = numShortestPaths(g, start, end)
    assert ret == 2


def singleVertexTest():
    """This method tests a special case, and checks that 
    the number of shortest paths in a graph with one vertex 
    and no edges is 1.
    """
    g = MyGraph()
    a = GraphVertex("a")
    g.insertVertex(a)
    assert numShortestPaths(g, a,a) == 1, "Error"


def exceptionsTest():
    """This method checks that the numShortestPaths.py will 
    throw a InvalidInputException when the input nodes or graph
    are not valid.
    """
    with pytest.raises(InvalidInputException):
        g = v0 = v1 = None
        # raises exception because graph and vertices are None.
        numShortestPaths(g, v0, v1)

    with pytest.raises(InvalidInputException):
        g = MyGraph()
        v0 = GraphVertex("v0")
        v1 = GraphVertex("v1")
        e0 = GraphEdge("e0", 1)
        # raises exception because v0, v1 are not vertices of g.
        numShortestPaths(g, v0, v1)


def get_tests():
    # DO NOT remove either example test from this list, just add new tests like so:
    #       [example, example, new test,...]
    return [sample_test, test1, singlePathTest, multiplePathsTest, 
    complicatedPathsTest, singleVertexTest, exceptionsTest]


# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print('Running tests...')
    for test in get_tests():
        test()
    print('All tests passed!')
