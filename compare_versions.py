class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """Purpose: Compares two version numbers. 
        If version1 > version 2 return 1;
        elif version2 > version 1 return -1;
        else: return 0.

        """
        i = 0
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]

        m = max(len(v2), len(v1))
        v1 = v1 + [0]*(m-len(v1))
        v2 = v2 + [0]*(m-len(v2))

        while i < len(v1):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i+= 1
        return 0
    