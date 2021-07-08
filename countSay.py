class Solution:
    def countSay(n):
        # Purpose: iterate 'saying' a digit string n times.

        s = '1'
        for i in range(n-1):
            first = s[0]
            new_string = ''
            count = 0

            for c in s:
                if first == c:
                    count += 1
                else: # if new letter, set first to c
                    new_string  +=  str(count) + first
                    first = c
                    count = 1

            new_string += str(count) + first
            s = new_string
        return s
