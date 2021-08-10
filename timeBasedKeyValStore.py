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


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)