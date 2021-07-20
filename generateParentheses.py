class Solution:
	def generateParentheses(self, n:int) -> List[str]:
		"""
		Purpose: Given n pair of parentheses, generates all possible 
		combinations of well-formed parentheses.

		Depth-first traversal
		"""
		def traverse(left, right, res):
			if right > left: return

			if left <= 0 and right <= 0:
				return self.ans.append(res)

			if left > 0:
				traverse(left-1, right, res + ")")

			if right > 0:
				traverse(left, right-1, res + "(")

		self.ans = []
		traverse(n, n, "")

		return self.ans