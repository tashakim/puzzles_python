class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Purpose: Returns the input string s with all invalid parentheses removed.
        """
        temp = []
        # we have one stack
        my_stack = []
        hanging_p = []
        # scan string from left to right, for each character add it to temp EXCEPT when count increases.
        for i,c in enumerate(s):
            temp.append(c)
        # if stack is empty and we get '(': add it to the stack
            if len(my_stack) == 0:
                if c == '(':
                    my_stack.append([c,i])
                elif c == ')':
                    hanging_p.append(i)
                    
        # if top of stack is not '(' and we get ')': don't add to stack, increase count by 1
            elif my_stack[-1][0] != '(' and c == ')':
                hanging_p.append(i)
        # if top of stack is '(' and we get ')': pop from top of stack
            elif my_stack[-1][0] == '(' and c == ')':
                my_stack.pop()
        # if top of stack is '(' and we get '(': add '(' to stack, continue
            elif my_stack[-1][0] == '(' and c == '(':
                my_stack.append([c,i])
        if my_stack:
            for item in my_stack:
                hanging_p.append(item[1])
            
        for item in reversed(hanging_p):
            del temp[item]
        # at the end, increase count by the no. of items left in stack.
        return "".join(temp)