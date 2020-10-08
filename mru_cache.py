class MRUCache:
    """
    Purpose: MRU caching policy discards the most recently used items first. 
    In findings presented at the 11th VLDB conference, Chou and DeWitt noted that 
    "when a file is being repeatedly scanned in a [Looping Sequential] reference pattern, 
    MRU is the best replacement algorithm". Subsequently, other researchers presenting at 
    the 22nd VLDB conference noted that for 'random access patterns' and 'repeated scans 
    over large datasets', MRU cache algorithms have more hits than LRU due to their tendency 
    to retain older data. 

    In other words, MRU algorithms are most useful in situations where the older an item is, 
    the more likely it is to be accessed.
    """

    def __init__(self, capacity: int):
        """
        Purpose: Initializes an MRU Cache with positive size capacity.
        """
        self.capacity = capacity
        self.cache = dict()
        self.MRU = []
        
    
    def get(self, key: int) -> int:
        """
        Purpose: Returns the value of the key if key exists.
        """
        if key in self.cache:
            self.MRU.remove((key, self.cache[key]))
            self.MRU.append((key, self.cache[key]))
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        """
        Purpose: Updates the value of the key if the key exists. 
        Otherwise, add the key-value pair to the cache. 
        If the number of keys exceeds the capacity from this operation, 
        evict the most recently used key.
        """
        if key not in self.cache:
            self.MRU.append((key, value))
        else:
            self.MRU.remove((key, self.cache[key]))
            self.MRU.append((key, value))
        self.cache[key] = value
        
        if len(self.MRU) > self.capacity:
            popped = self.MRU.pop()[0]
            self.cache.pop(popped)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)