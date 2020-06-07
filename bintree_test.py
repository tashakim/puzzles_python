# Tests for binary tree, and node ADT
import pytest
import bintree_imp
from bintree_imp import *

def simpleTest():
	t = BinTree()
	t.addRoot("A")

	assert(t.root().value() == "A"), "Wrrong value"

def get_tests():
	return [simpleTest]

if __name__ == "__main__":
	print("Running tests...")
	for item in get_tests():
		item()

	print("All tests passed!")