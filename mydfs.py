def depthfirst(r):
	s = list()
	s.append(r)
	visited = []

	while s not empty:
		visited.append(s.pop(0))
		s.append(r.left())
		s.append(r.right())

if __name__ == "__main__":
	depthfirst(root)
