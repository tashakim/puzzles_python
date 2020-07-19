class Solution:
    def maximum69Number (self, num: int) -> int:
        s, count = [], 0
        num = str(num)

        for i in range(len(num)):
            if num[i] == '9':
                s.append('9')
                count += 1
            elif num[i] == '6':
                s.append('9')
                break

        for i in range(count+1, len(num)):
            s.append(str(num[i]))

        return "".join(s)

    def maximum69Number(self, num):
        """Python one-liner """
        return int(str(num).replace('6', '9', 1))