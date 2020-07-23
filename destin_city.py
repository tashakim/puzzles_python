class Solution:
    def destCity0(self, paths: List[List[str]]) -> str:
        mydict = {}
        for p in paths:
            for i in range(2):
                if p[i] not in mydict:
                    mydict[p[i]] = i
                else:
                    mydict.pop(p[i])
        l = [k for k, v in mydict.items() if v == 1]
        return l.pop()
        