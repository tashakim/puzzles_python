class Solution:
    def fizzBuzz0(self, n: int) -> List[str]:
        # TC: O(n), SC: O(1)
        res = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                res.append("FizzBuzz")
            elif i%3==0:
                res.append("Fizz")
            elif i%5==0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

    def fizzBuzz(self, n):
        # String concatenation! 
        # TC: O(n
        ans = []
        
        for i in range(1, n+1):
            res = ""
            if i%3 == 0:
                res += "Fizz"
            if i%5 == 0:
                res += "Buzz"
            if not (i%3==0 or i%5==0):
                res += str(i)
            ans.append(res)
        return ans


    def fizzBuzz(self, n: int) -> List[str]:
        mydict = {3: "Fizz", 5: "Buzz"}
        res = []
        for i in range(1, n+1):
            mystr = ""
            for k, v in mydict.items():
                if i%k == 0:
                    mystr += v
            if mystr == "": mystr = str(i)
            res.append(mystr)
        return res
                    