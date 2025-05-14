#!/usr/bin/env python3

"""FIFO cache implementation"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    def __init__(self):
        """Initialize the class using BaseCaching constructor"""
        super.__init__()
        self.order = []

    def put(self, key, item):
        """
        Add a new key-item pair in cache_data
        Also checks if limit has been exceeded
        if so, discard first item in cache_data
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a value based on the key.
        If key is None or non existent, return none
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
