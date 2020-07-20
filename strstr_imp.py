class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Purpose: Python implementation of the strstr()
        function."""

        if needle == "":
            return 0
        ptr = 0
        while ptr < len(haystack):
            if needle[0] == haystack[ptr]:
                if needle in haystack[ptr:ptr+len(needle)]:
                    return ptr
            ptr += 1
        return -1