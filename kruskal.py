from mygraph import *
from heappriorityqueue import *

def kruskal(g):
	#Input: 
	#Output:
	for v in g.vertices():
		make_cloud(v)
	min_spanning_tree = []
	# sort all edges here
	for e in g.edges(): # edge between u and v
		# if u and v not in same cloud:
			# a add edge to min_spanning_tree
			# merge clouds containing u and v

	return min_spanning_tree

def make_cloud(v):
	parent[v] = v
	rank[v] = 0

def cloud(a,b):
	A = find(a)
	B = find(b)
	parent[A] = B

def find(A):
	while parent[A] != A:
		A = parent[A]
	return A