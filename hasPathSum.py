def hasPathSum(root, sum):
	"""Purpose: Checks if a binary tree has a root-to-leaf path that 
	adds up to sum.
	"""
	if not root: return False
	sum -= root
	# stop search when we reach leaf 
	if not root.left or not root.right:
		return sum == 0

	return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)


if __name__ == "__main__":
	#hasPathSum()