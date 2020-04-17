def prim(g):
	# Purpose: Implementation of the prim-jarnik algorithm
	# Input: weighted, undirected graph g with vertices v
	# Output: list of edges in the minimum spanning tree
	for v in g.vertices():
		v._cost = float('inf')
		v._prev = None


	#source = random vertex in g.vertices()
	source._cost = 0
	min_spanning_tree = []
	# Q = priorityQueue(vertex)
	while Q is not None:
		vertex = Q.removeMin()
		if vertex._prev != None:
			min_spanning_tree.append((vertex, vertex._prev))
		# for edges (vertex,u) of vertex such that u is in Q:
			# if u._cost > edge (v,u)._weight:
				# u._cost = edge (v,u)._weight
				# u._prev = vertex
				# Q.decreaseKey(u, u._cost)
	return min_spanning_tree