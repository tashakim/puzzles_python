from mygraph import *
from heappriorityqueue import *

def kruskal(g):
	#Input: 
	#Output:
	for v in g.vertices():
		# make cloud for v
	min_spanning_tree = []
	# sort all edges here
	for e in g.edges(): # edge between u and v
		# if u and v not in same cloud:
			# a add edge to min_spanning_tree
			# merge clouds containing u and v

	return min_spanning_tree

def cloud(a,b):
	A = find(a)
	B = find(b)
	parent[A] = B

def find(A):
	while parent[A] != A:
		A = parent[A]
	return A