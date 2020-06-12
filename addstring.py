class InvalidInputException:
	pass

class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        if(isinstance(num1, str)!=True or !isinstance(num2, str)!=True):
        	raise InvalidInputException("Input is invalid.")
       
       return str(int(num1) + int(num2))


if __name__ == "__main__":
	s = Solution()
	assert(s.addStrings("0","0") == "0"), "Wrong answer."
