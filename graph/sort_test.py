#!/usr/bin/python3

# DO NOT DELETE THESE STATEMENTS
import sort
from importlib import reload
reload(sort)
from sort import *
import pytest

# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.


def example_test_1():
    """This method is a sample test that checks correct 
    outputs are given using this program.
    """
    assert 1 == 1, 'Error: 1 does not equal 1!'


def simple_test():
    # This loops through all of your sort algorithms, and
    # runs any asserts in the for loop on each one.
    sort_algorithms = [(merge_sort, "Merge sort"), (quick_sort, "Quick sort"), 
    (radix_sort, "Radix sort")]
    for sort_algorithm, name in sort_algorithms:
        assert sort_algorithm([4,5,1,3,2]) == [5,4,3,2,1], "%s failed." % name


def positiveIntegerTests():
    """This method checks that all the sorting algorithms 
    correctly order an array of positive integers in descending
    order.
    """
    sort_algorithms = [(merge_sort, "Merge sort"), (quick_sort, "Quick sort"), 
    (radix_sort, "Radix sort")]
    for sort_algorithm, name in sort_algorithms:
        assert sort_algorithm([1,2,3]) == [3,2,1], "%s failed." % name
        assert sort_algorithm([0,0,2]) == [2,0,0], "%s failed." % name
        assert sort_algorithm([0,1,2,3,4,5]) == [5,4,3,2,1,0], "%s failed." %name


def invalidInputExceptionTest():
    """This method checks that sort.py correctly throws an 
    InvalidInputException when the input array is None.
    """
    with pytest.raises(InvalidInputException):
        merge_sort(None)
        quick_sort(None)
        radix_sort(None)


def repeatingElementsTests():
    """This method checks that all the sorting algorithms 
    correctly order an array containing repeated integers in 
    descending order.
    """
    sort_algorithms = [(merge_sort, "Merge sort"), (quick_sort, "Quick sort"), 
    (radix_sort, "Radix sort")]
    for sort_algorithm, name in sort_algorithms:
        assert sort_algorithm([1,1]) == [1,1], "%s failed." % name
        assert sort_algorithm([2,1,2]) == [2,2,1], "%s failed." % name
        assert sort_algorithm([9,3,7,3]) == [9,7,3,3], "%s failed." % name
        assert sort_algorithm([0,0,0,3,3]) == [3,3,0,0,0], "%s failed." % name
        assert sort_algorithm([0,2,0,2,0,3,2,3]) == [3,3,2,2,2,0,0,0], "%s failed." % name


def emptyListTest():
    """This method tests that if an empty array [] is input into
    any of our sorting algorithms, the output will also be an empty
    array [].
    """
    sort_algorithms = [(merge_sort, "Merge sort"), (quick_sort, "Quick sort"), 
    (radix_sort, "Radix sort")]
    for sort_algorithm, name in sort_algorithms:
        assert sort_algorithm([]) == [], "%s failed." % name


def singleElementTest():
    """This method checks that if an integer array has only one element,
    then all of our sorting algorithms will return the same array.
    """
    sort_algorithms = [(merge_sort, "Merge sort"), (quick_sort, "Quick sort"), 
    (radix_sort, "Radix sort")]
    for sort_algorithm, name in sort_algorithms:
        assert sort_algorithm([0]) == [0], "%s failed." % name
        assert sort_algorithm([3]) == [3], "%s failed." % name
        assert sort_algorithm([-9]) == [-9], "%s failed." % name


def negativeElementsTest():
    """This method checks that all our implementations of the three 
    sorting algorithms can sort negative integers as well as zero 
    and positive integers into descending order.
    """
    sort_algorithms = [(merge_sort, "Merge sort"), (quick_sort, "Quick sort"), 
    (radix_sort, "Radix sort")]
    for sort_algorithm, name in sort_algorithms:
        assert sort_algorithm([-1, -2, 3]) == [3,-1,-2], "Failed negative int test"
        assert sort_algorithm([-1, -2, 0, 3]) == [3,0,-1,-2], "%s failed." % name
        assert sort_algorithm([-8,0,-5,-1,9,9,-8]) == [9,9,0,-1,-5,-8,-8], "%s failed." % name


def get_tests():
    # Add the names of each of your test functions to this list. It is very
    # important that you do this, or the TAs will not run your tests properly
    # and you will not receive full credit.
    #
    # DO NOT remove either example test from this list, just add new tests like so:
    #       [example, example, new test,...]
    # We will not be able to properly grade your coal tests if you do not follow
    # these instructions! You will lose points on your submission for failing
    # to follow these instructions.
    return [example_test_1, simple_test, invalidInputExceptionTest, repeatingElementsTests, 
    emptyListTest, singleElementTest, negativeElementsTest, positiveIntegerTests]

# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print('Running tests...')
    for test in get_tests():
        test()
    print('All tests passed!')
