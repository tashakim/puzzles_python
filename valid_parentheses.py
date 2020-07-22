class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {'(': ')', '[':']', '{':'}'}
        mystack = []
        res = ""
        for c in s:
            if c in mydict:
                res += c
                mystack.append(mydict[c])
            else:
                if mystack:
                    res += mystack.pop()

        for x in range(len(mystack)):
            res += mystack.pop()
        return res == s