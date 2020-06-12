class InvalidInputException:
	pass

class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        #if(isinstance(num1, str) or isinstance(num2, str)):
        	#raise InvalidInputException("Input is a string.")
       
       return str(int(num1) + int(num2))


if __name__ == "__main__":
	s = Solution()
	assert(s.addStrings("0","0") == "0"), "Wrong answer."
	assert(s.addStrings("10","1") == "11"), "Wrong answer."
	assert(s.addStrings("1000", "11", "89"), "1100"), "Wrong answer."
	print("All tests passed!")