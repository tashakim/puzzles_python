class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    """Purpose: Recursively increments the input digit.

    Example: [1,2,3] -> [1,2,4]
    [4,3,2,1] -> [4,3,2,2]
    """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits