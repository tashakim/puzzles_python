import pytest
import random
from typing import Any
from ddl_lru_cache import DoublyLinkedList
from ddl_lru_cache import ListNode

# %% [markdown] {"colab_type": "text", "id": "Z23HcXnk17kG"}
# # LRU Cache 
# This project should help familiarize you with two kinds of data structures: doubly linked lists and dictionaries. In this project, you'll implement a Least Recently Used (LRU) Cache comprised of these two data structures. 
#
# %% [markdown] 
# Task3.2 Finish LRUCache

class LRUCache:
    """
    A "Least Recent Used" cache. This cache holds 
    up to `capacity` key-value pairs. Adding a new key when the cache is full (via put)
    results in the least recently key-value pair is removed.
    """

    def __init__(self, capacity=4):
        '''Create a LRUCache with of size capacity.'''
        if capacity < 1:
            raise ValueError(
                "capacity should be >=1 but {} given".format(capacity))
        self.capacity = capacity

        # This linked list records the key-value pair in the order of their recentness.
        self.list = DoublyLinkedList()

        # dictionay that maps keys to linked list node for quicker node lookup
        self.map = {}

    def __len__(self):
        return len(self.list)

    def __contains__(self, key):
        """ Magic method for checking key existence

        Examples: 
            if 'key' in lru_dict:
                print("exist!")
        """
        return key in self.map

    def put(self, key, value):
        """
        Adds (key, value) to cache. If the cache is full, and the key is new,
        the least recently (key,value) pair is removed.
        """
        # If the key already exists in the self.map dict,
        # replace the key-value pair stored in the linked list. 
        # If the key does not exist, add this key-value pair to self.list.  If
        # self.map is over capacity, evict the least recent used key-value.
        # Also be sure to update the LRU order in self.list.

        if key in self.map:
            self.list.remove(self.map[key])
        new_node = ListNode((key, value))
        self.list.prepend(new_node) # Add new node to order list
        self.map[key] = new_node # Add new node to hash table

        # If hash table overflows, evict the LRU key-value.
        if len(self.map) > self.capacity:
            new_node = self.head.next
            self.list.remove(new_node) # Pop node that stores key-value pair from order list
            self.map.pop(new_node[0], None) # Pop key-value pair from hash table
        

    def get(self, key, default=None):
        """
        Get value for `key`. Return `default` when the key is not found.
        """
        # If the key exists in self.map, return the value and update the LRU order in self.list.
        # If the key does not exist return the default value.
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            self.list.prepend(node)
            return node.data[1]

        return default


    def items(self):
        """
        Return all key-value pairs in the order of recentness (the most recent to the least recent)
        """
        res = []
        cur_node = self.list.head.next
        while cur_node.next:
            res.append(cur_node.data)
            cur_node = cur_node.next
        return res


    def __str__(self):
        """
        Return str representation of self.items()
        """
        return "LRUCache:\n" + '\n'.join([f"key={k}, value={v}" for k, v in self.items()])


# Task3.3 Testing

class DefaultValue:
    def __eq__(self, other):
        return isinstance(other, DefaultValue)

def assert_miss(d, key):
    assert key not in d.map
    assert isinstance(d.get(key, DefaultValue()), DefaultValue)


def test_example():
    ld = LRUCache(2)
    assert_miss(ld, 'a')        # should miss
    ld.get(3, None)
    

def test_list_repr_with_cycle():
    # help boosting coverage by testing LinkedList.__str__
    l = DoublyLinkedList()
    last = ListNode(3)
    l.prepend(last)
    l.prepend(ListNode(2))
    first = ListNode(1)
    l.prepend(first)
    last.next = first
    assert str(l) == "None -> 1 -> 2 -> 3 -> 1 -> ... -> 1 -> ..."

# TODO: add your tests below this line

if __name__ == "__main__":
    ld = LRUCache()
    ld.put(1,1)
    print(ld.items())
    print(ld.list)
    ld.put(2,2)
    print(ld.items())
    print(ld.list)
    ld.put(2,3)
    print(ld.items())
    print(ld.list)
    print(ld.get(2))
    print(ld.get(1))
    ld.put(5,5)
    print(ld.list)
    print(ld.items())
    test_example()
    print("Passed all tests")
    test_example()
    test_list_repr_with_cycle()




# execute this cell to start the test.
#!pytest --cov-report term --cov-report=annotate LRUCache.py --cov .

