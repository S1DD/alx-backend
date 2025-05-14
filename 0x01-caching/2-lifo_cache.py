#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.last_item = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            item_len = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.last_item[-1]))
                del self.cache_data[last_item[-1]]
                del self.last_item[-1]
            if key in self.lastitem:
                del self.last_item[self.last_item.index(key)]
            self.lastitem.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value associated to a specified key, or None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
