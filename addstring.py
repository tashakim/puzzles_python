class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


if __name__ == "__main__":
	s = Solution()
	assert(s.addStrings("0","0") == "0"), "Wrong answer."
