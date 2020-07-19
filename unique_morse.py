class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m,a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."], "abcdefghijklmnopqrstuvwxyz"
        l = set()
        for s in words:
            res = ""
            for c in s:
                res += m[a.index(c)]
            l.add(res)
        return len(l)
            
            
if __name__ == "__main__":
	assert(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2), "Wrong answer."
	print("Test passed!")