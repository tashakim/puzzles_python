class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
    	"""Purpose: Returns the average of each student's top
    	five scores, in order of each student's id.
    	"""
        count, d = 0, {}
        for x in items:
            if x[0] not in d:
                d[x[0]] = [x[1]]
            else:
                d[x[0]].append(x[1])

        return [[k, sum(sorted(v)[-5:])//5] for k,v in d.items()]