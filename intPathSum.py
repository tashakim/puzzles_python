class Solution:
    def pathSum(self, nums: List[int]) -> int:
        """
        Purpose: Given an array of ascending integers `nums` representing binary tree, 
        returns the sum of all paths from the root towards the leaves.

                    4
                1       5
              1    2  3    1

        => (4+1+1) + (4+1+2) + (4+5+3) + (4+5+1) = 35

        """
        d = {} # tree
        for x in nums:
            d[str(x)[:2]] = str(x)[2] 
        visited = set()

        def traverse(i, j, cur_sum=0):
            """
            Purpose: Traverses integer binary tree coordinates in depth-first search way.
            
            """
            cur_position = str(i) + str(j)
            if cur_position not in d: return
            if (i,j) not in visited:
                visited.add((i,j))
                next_position1 = str(i+1) + str(2*j-1) # left node 
                next_position2 = str(i+1) + str(2*j) # right node
                
                if (next_position1 not in d and next_position2 not in d):
                    self.res += (cur_sum + int(d[cur_position]))
                    return

                traverse(i+1, 2*j-1, cur_sum + int(d[cur_position]))
                traverse(i+1, 2*j, cur_sum + int(d[cur_position]))
            else: pass
            
        self.res = 0
        traverse(1, 1, 0)
        return self.res