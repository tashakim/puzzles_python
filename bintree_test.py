# Tests for binary tree, and node ADT
import pytest
import bintree_imp
from bintree_imp import *

def simpleTest():
	t = BinTree()
	t.addRoot("A")

	assert(t.root().value() == "A"), "Wrrong value"
# add more tests here
def exceptionTest():
	"""Purpose: Tests that the binary tree module throws 
	correct Exceptions.
	"""
	t2.BinTree()
	with pytest.raises(InvalidInputException):
		###
		


def get_tests():
	return [simpleTest] # add tests to list

if __name__ == "__main__":
	print("Running tests...")
	for item in get_tests():
		item()

	print("All tests passed!")