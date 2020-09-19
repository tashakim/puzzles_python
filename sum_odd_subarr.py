class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        window_length, res = 1, 0
        while window_length <= len(arr):
            i = 0
            while i + window_length <= len(arr):
                res += sum(arr[i:i+window_length])
                i += 1
            window_length += 2

        return res