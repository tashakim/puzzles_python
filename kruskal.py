from mygraph import *
from heappriorityqueue import *


def kruskal(g):
	#Input: 
	#Output:
	for v in g.vertices():
		make_cloud(v)
	min_spanning_tree = []
	g.edges().sort()
	for e in g.edges(): # edge between u and v
		# if u and v not in same cloud:
		if find(u) != find(v):
			# a add edge to min_spanning_tree
			minimum_spanning_tree.add(edge)
			# merge clouds containing u and v
			cloud(u,v)

	return min_spanning_tree

def make_cloud(v):
	parent[v] = v
	rank[v] = 0

def cloud(u,v):
	A = find(a)
	B = find(b)
	if A != B:
		if rank[u]>rank[v]:
			parent[v] = u
		else:
			parent[u] = v
		if rank[u] == rank[v]:
			rank[v] = rank[v]+1

def find(v):
	if parent[v] != v:
		parent[v] = find(parent[v])
	return parent[v]

if __name__ == "__main__":
	g = MyGraph()
	my_tree = kruskal(g)
	my_tree.mygraph()
