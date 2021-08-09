class Solution:
    def arrayRankTransform0(self, arr: List[int]) -> List[int]:
        """
        Purpose: Replaces each element in integer array with its rank.

        Note: 
        - Rank is an integer starting from 1;
        - The larger the element, the larger the rank;
        - If two elements are equal, their rank must be the same;
        - Rank should be as small as possible.

        """
        elements = set(arr)
        sorted_ranks = sorted(list(elements))

        res = []
        for x in arr:
            res.append(sorted_ranks.index(x) + 1)
            
        return res


    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Improves time complexity of solution above, by using hash table to keep track of rank.

        """
        elements = list(set(arr))
        sorted_ranks = sorted(elements)

        d = {}
        for i, x in enumerate(sorted_ranks): 
            d[x] = i + 1
            
        res = []
        for x in arr: 
            res.append(d[x])
            
        return res