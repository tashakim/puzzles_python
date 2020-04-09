def minSem(g):
	"""Purpose:
	Input: A directed acyclic graph (DAG) with courses
	Output: Integer, minimum number of semesters to complete the curriculum.
	"""
	for i in g.iterVertices():
		i._vertex = 0
		i._semesters = 0
	for i in g.iterVertices:
		i._indegree = size(i.incidentEdges())
		if i._indegree == 0:
			Queue.append(i)
	while Queue != None:
		elem = Queue.pop(0)
		for i in elem.incidentVertices():
			i._indegree -= 1
			i._semesters = 1 + elem._semesters
			if i._indegree == 0:
				Queue.append(i)
		minimum = max(semesters)
		
	return minimum