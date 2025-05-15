#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    def __init__(self):
        """
        Initialize the class with the parent's init method
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
                last_key = self.cache_data.popitem(True)
                print(f"DISCARD: {last_key}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Return the value associated to a specified key, or None
        """

        return self.cache_data.get(key, None)
