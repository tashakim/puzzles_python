class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        max_count = 0
        temp = [1]*len(pairs)
        pairs.sort()
        
        for i in range(1, len(pairs)):
            for j in range(i):
                if(pairs[i][0] > pairs[j][1]):
                    temp[i] = temp[j] + 1
            if(max_count < temp[i]):
                max_count = temp[i]
                
        return max_count
        