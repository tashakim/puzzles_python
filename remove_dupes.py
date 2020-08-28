class Solution:
    def removeDuplicates0(self, S: str) -> str:
        """Purpose: Removes all duplicate characters in a string
        until there are none.

        Example: 'abbaccd' -> 'aaccd' -> 'ccd' -> 'd'.

        Time Complexity: O(n)
        Space Complexity: O(n - d), n is length of S, d is length of 
        all duplicates, hence d < n for all d.

        Very beautiful example of when stacks are helpful!
        """
        my_stack = []
        for c in S:
            if not my_stack or c != my_stack[-1]:
                my_stack.append(c)
            elif c == my_stack[-1]:
                my_stack.pop()
        return "".join(my_stack)
    
    
    def removeDuplicates(self, S):
        """Purpose: Utilizes more space (hash set), but is even slower!
        """
        my_dict = set(2*c for c in ascii_lowercase)
        n = float('inf')
        while n != len(S):
            n = len(S)
            for cc in my_dict:
                S = S.replace(cc, "")
        return S