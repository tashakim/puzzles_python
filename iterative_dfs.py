# iteratively
def preorderTraversal(self, root):
    visited, order = [root], []
    while visited:
        p = visited.pop()
        order.append(p.val)
        if p.right:
            visited.append(p.right)
        if p.left:    
            visited.append(p.left)
    return res

# iteratively        
def postorderTraversal(self, root):
    visited, order = [root], []
    while visited:
        p = visited.pop()
        order.append(p.val)
        if p.left:
	        visited.append(p.left)
    	if p.right:
        visited.append(p.right)
    return order[::-1]


def bfs(self, root):
	visited, order = [root], []
	while visited:
		p = visited.pop(0)
		order.append(p.val)
		if p.left:	
			visited.append(p.left)
		if p.right:	
			visited.append(p.right)
	return order


# iteratively       
def inorderTraversal(self, root):
    visited, order = [], []
    while True:
        while root:
            visited.append(root)
            root = root.left
        if not visited:
            return order
        node = visited.pop()
        order.append(node.val)
        root = node.right   
