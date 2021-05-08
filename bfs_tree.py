def bfs(node):
# breadth first tree traversal using a queue.
	order = []
	visited = [root]
	while visited:
		popped = visited.pop(0)
		order.append(popped.val)
		if popped.left:
			visited.append(popped.left)
		if popped.right:
			visited.append(popped.right)

	return order


def dfs(node):
	if node:
		dfs(node.left)
		dfs(node.right)
		print(node)