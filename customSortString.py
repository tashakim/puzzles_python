from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str):
        res = [''] * len(s)
        d = {}
        i = 0
        for c in order:
            d[c] = i
            i += 1
        
        for c in s:
            if c in d:
                res[d[c]] =  d[c] * c 
            else:
                res.append(c)

        return ''.join(res)
            
    def customSortString2(self, order, s):
        counter = Counter(s)
        res = []
        for c in order:
            res.append( counter[c] * c )            
            counter[c] = 0

        for c in s:
            res.append( counter[c] * c)

        return ''.join(res)

    def customSortString3(self, order, s):
        return ''.join(sorted(s, key = lambda x: order.index(x) if x in order else -1))