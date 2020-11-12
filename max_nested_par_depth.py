class Solution:
    def maxDepth(self, s: str) -> int:
    """
    Purpose: Return the maximum nested depth of parentheses.
    Time complexity: O(n), where n is length of input string s
    Space complexity: O(n), where n is length of input string s
    """
        my_stack = []
        count, max_count = 0, 0
        for c in s:
            if c == '(':
                my_stack.append(c)
                count += 1
                
            elif c == ')':
                if my_stack[-1] == '(':
                    my_stack.pop()
                    count -= 1
            
            if max_count < count:
                max_count = count
                    
        return max_count