class ListNode:
    """Purpose: Chaining in hashmap.
    """
    def __init__(self, k, v):
        self.pair(k, v)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initializes the data structure.
        """
        self.capacity = 1000
        self.data = [None]*self.capcity


    def insert(self, k: int, v: int) -> None:
        """
        value will always be non-negative.
        """
        i = k % self.capacity
        if not self.data[i]:
            self.data[i] = ListNode(k, v)
        else:
            cur = self.data[i]
            while True:
                if cur.pair[0] == k:
                    cur.pair = (k, v)
                    return
                if not cur.next:
                    break
                cur = cur.next
            cur.next = ListNode(k, v)
        

    def get(self, k: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = k % self.capacity
        cur = self.data[i]
        while cur:
            if cur.pair[0] == k:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
        

    def delete(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = k % self.capacity
        cur = pre = self.data[i]
        if not cur:
            return
        if cur.pair[0] == k:
            self.data[i] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == k:
                    pre.next = cur.next
                    break
                else:
                    cur, pre = cur.next, pre.next

# The MyHashMap object is instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)