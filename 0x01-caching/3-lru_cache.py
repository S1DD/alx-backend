#!/usr/bin/env python3
"""
Task 3: LRU Caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache defines a LRU caching system
    """

    def __init__(self):
        """
        Initialize the class using the parent's init method
        """

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Cache a key-value pair
        """

        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lruKey = self.cache_data.popitem(True)
                print(f"DISCARD: {lruKey}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value based on the key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
