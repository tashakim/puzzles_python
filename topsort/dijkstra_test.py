#!/usr/bin/python3

# DO NOT DELETE THESE STATEMENTS
import dijkstra
from importlib import reload
reload(dijkstra)
from dijkstra import *
from mygraph import *
import pytest

# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.

# DO NOT write your tests within the example test functions we provide!
# Our scripts will skip the test functions we provide, so write your own
# functions to test your code thoroughly.

# Here are some example test functions. Feel free to delete example_test_1
# and remove it from the list in get_tests().


def example_test_1():
    assert 1 == 1, 'Error: 1 does not equal 1!'


def simple_test():
    # Setup simple graph
    g = MyGraph()
    v0 = GraphVertex("v0")
    v1 = GraphVertex("v1")
    v2 = GraphVertex("v2")
    g.insertVertex(v0)
    g.insertVertex(v1)
    g.insertVertex(v2)

    e0 = GraphEdge("e0", 8)
    e1 = GraphEdge("e1", 3)
    e2 = GraphEdge("e2", 4)
    g.insertEdge(v0, v2, e0)
    g.insertEdge(v0, v1, e1)
    g.insertEdge(v1, v2, e2)

    # Run the algorithm
    ret = dijkstra(g, v0)

    # Make sure it matches our expectations
    assert e1 in ret.edges()
    assert e2 in ret.edges()
    assert e0 not in ret.edges()
            
    # If necessary you can take a look at the graph
    # you created for testing and what was returned
    g.popup()
    ret.popup()


def vertexTest():
    """Purpose: This method tests that all the vertices from the 
    original graph are all in our resulting tree.
    """
    g = MyGraph()
    v0 = GraphVertex("v0")
    v1 = GraphVertex("v1")
    v2 = GraphVertex("v2")
    g.insertVertex(v0)
    g.insertVertex(v1)
    g.insertVertex(v2)

    e0 = GraphEdge("e0", 8)
    e1 = GraphEdge("e1", 3)
    e2 = GraphEdge("e2", 4)
    g.insertEdge(v0, v2, e0)
    g.insertEdge(v0, v1, e1)
    g.insertEdge(v1, v2, e2)

    # Run the algorithm
    ret = dijkstra(g, v0)

    # Make sure it matches our expectations
    assert v0 in ret.vertices()
    assert v1 in ret.vertices()
    assert v2 in ret.vertices()


def notInGraphTest():
    """Purpose: This method tests that the edges that are not
    in our output minimum spanning tree from our dijkstra algorithm.
    """
    g = MyGraph()
    v0 = GraphVertex("v0")
    v1 = GraphVertex("v1")
    v2 = GraphVertex("v2")
    v3 = GraphVertex("v3")
    v4 = GraphVertex("v4")
    g.insertVertex(v0)
    g.insertVertex(v1)
    g.insertVertex(v2)
    g.insertVertex(v3)
    g.insertVertex(v4)

    e0 = GraphEdge("e0", 1)
    e1 = GraphEdge("e1", 1)
    e2 = GraphEdge("e2", 1)
    e3 = GraphEdge("e3", 1)
    e4 = GraphEdge("not", 100)
    e5 = GraphEdge("not2", 999)

    g.insertEdge(v0, v1, e0)
    g.insertEdge(v1, v2, e1)
    g.insertEdge(v2, v3, e2)
    g.insertEdge(v3, v4, e3)
    g.insertEdge(v0, v4, e4)
    g.insertEdge(v0, v3, e5)

    ret = dijkstra(g, v0)
    assert e4 not in ret.edges()
    assert e5 not in ret.edges()


def singleNodeTest():
    """This method tests that an input graph that only has
    one vertex will return the vertex as an output of our 
    dijkstra algorithm.
    """
    g = MyGraph()
    v0 = GraphVertex("v0")
    g.insertVertex(v0)

    ret = dijkstra(g, v0)

    assert v0 in ret.vertices()
    assert ret.vertices() is not None


def largeGraphInputTest():
    """Purpose: This method tests that the dijkstra algorithm 
    gives the correct output for a large graph with multiple 
    edges and nodes.
    """
    g = MyGraph()
    A = GraphVertex("A")
    B = GraphVertex("B")
    C = GraphVertex("C")
    D = GraphVertex("D")
    E = GraphVertex("E")
    F = GraphVertex("F")

    g.insertVertex(A)
    g.insertVertex(B)
    g.insertVertex(C)
    g.insertVertex(D)
    g.insertVertex(E)
    g.insertVertex(F)

    e0 = GraphEdge("e0", 5)
    e1 = GraphEdge("e1", 2)
    e2 = GraphEdge("e2", 9)
    e3 = GraphEdge("e3", 2)
    e4 = GraphEdge("e4", 3)
    e5 = GraphEdge("e5", 2)
    e6 = GraphEdge("e6", 3)

    g.insertEdge(A, B, e0)
    g.insertEdge(A, E, e1)
    g.insertEdge(A, D, e2)
    g.insertEdge(B, C, e3)
    g.insertEdge(C, D, e4)
    g.insertEdge(D, F, e5)
    g.insertEdge(E, F, e6)

    ret = dijkstra(g, A)

    assert e0 in ret.edges()
    assert e3 in ret.edges()
    assert e1 in ret.edges()
    assert e6 in ret.edges()
    assert e5 in ret.edges()

    g.popup()
    ret.popup()


def invalidInputTest():
    """Purpose: This method tests that the dijkstra algorithm raises
    the appropriate Exception('InvalidInputException') when invalid 
    graph components / graph are given.
    """
    # raises Exception when graph or source node are None.

    with pytest.raises(InvalidInputException):
        v0 = GraphVertex("v0")
        dijkstra(None, v0)

    # raises Exception when the source node is not part of input graph.

    with pytest.raises(InvalidInputException):
        g = MyGraph()
        v0 = GraphVertex("v0")
        g.insertVertex(v0)
        dijkstra(g, v1)

            
def get_tests():
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # VERY IMPORTANT
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Add the names of each of your test functions to this list. It is very
    # important that you do this, or the TAs will not run your tests properly
    # and you will not receive full credit.
    #
    # DO NOT remove either example test from this list, just add new tests like so:
    #       [example, example, new test,...]
    # We will not be able to properly grade your coal tests if you do not follow
    # these instructions! You will lose points on your submission for failing
    # to follow these instructions.
    return [example_test_1, simple_test, vertexTest, notInGraphTest, singleNodeTest, 
    largeGraphInputTest, invalidInputTest]

# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print('Running tests...')
    for test in get_tests():
        test()
    print('All tests passed!')
