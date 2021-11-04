def validTree(n, edges):
	graph = [[] for x in range(n)]
	for x,y in edges:
		graph[x].append(y)
		graph[y].append(x)
		
	self.visited = set()
	self.res = True

	def traverse(node, seen, prev):
		if not graph[node]: 
			if node in seen: # loop detected
				self.res = False
			return

		self.visited.add(node)
		seen.add(node)

		for x in graph[node]:
			if x != prev:
				if x in seen:
					self.res = False
					return
				traverse(x, seen, node)

	if not edges: 
		return n <= 1
	root = edges[0][0]
	traverse(root, set(), None)

	return self.res and len(self.visited) == len(graph)
				