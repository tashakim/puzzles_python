class friends:
	def findFriendcirc(self, M: List[List[int]]) -> int:
		count = 0
		visited = []
		for i in range(len(M)):
			if i not in visited:
				count += 1
				self.dfs(M, i, visited)
		return count

	def dfs(self, M, i, visited):
		for i, friends in enumerate(M[i]):
			if(friends and i not in visited):
				visited.append(i)
				dfs(M, i, visited)
