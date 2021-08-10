class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache: 
            self.cache[key] = [[timestamp, value]]
        else: 
            self.cache[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache or timestamp < self.cache[key][0][0]: 
            return ""
        
        for k in reversed(self.cache[key]):
            if k[0] <= timestamp: 
                return k[1]


from collections import defaultdict

class TimeMap(object): 
    """
    Purpose: Improves time complexity, implements binary search.

    """
    def __init__(self):
        self.cache = defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.cache[key].append([timestamp, value])


    def get(self, key, timestamp):
        arr = self.cache[key]
        left, right = 0, len(arr)

        if right == 0: return ""
         
        while left < right:
            mid = (left + right) / 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid
        
        return arr[right - 1][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)