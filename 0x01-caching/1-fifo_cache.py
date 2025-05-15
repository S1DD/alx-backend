#!/usr/bin/env python3

"""FIFO cache implementation"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):

    def __init__(self):
        """Initialize the class using BaseCaching constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add a new key-item pair in cache_data
        Also checks if limit has been exceeded
        if so, discard first item in cache_data
        """
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a value based on the key.
        If key is None or non existent, return none
        """
        return self.cache_data.get(key, None)
