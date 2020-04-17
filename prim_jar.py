def prim(g):
	# Purpose: Implementation of the prim-jarnik algorithm
	# Input: weighted, undirected graph g with vertices v
	# Output: list of edges in the minimum spanning tree
	for v in g.vertices():
		