#!/usr/bin/env python3

from base_caching import BaseCaching
from collections import OrderedDict

class LFUCache(BaseCaching):
    """
    LFUCache defines a Least Frequently Used caching system
    """

    def __init__(self):
        """
        Initialize class with the base class's init method
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keyFrequency = []

    def reorganize_items(self, mruKey):
        """Reorganizes the items in the cache based on the most
        recently used item.
        """
        maxPos = []
        mruFrequency = 0
        mruPos = 0
        index = 0
        for i, keyFrequency in enumerate(self.keyFrequency):
            if keyFrequency[0] == mruKey:
                mruFrequency = keyFrequency[1] + 1
                mruPos = i
                break
            elif len(maxPos) == 0:
                maxPos.append(i)
            elif keyFrequency[1] < self.keyFrequency[maxPos[-1]][1]:
                maxPos.append(i)
        maxPos.reverse()
        for pos in maxPos:
            if self.keyFrequency[pos][1] > mruFrequency:
                break
            index = pos
        self.keyFrequency.pop(mruPos)
        self.keyFrequency.insert(index, [mruKey, mruFrequency])

    def put(self, key, item):
        """
        Cache a key-value pair
g       """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfuKey = self.keyFrequency[-1]
                self.cache_data.pop(lfuKey)
                self.keyFrequency.pop()
                print(f"DISCARD: {lfuKey}")
            self.cache_data[key] = item
            index = len(self.keyFrequency)
            for i, keyFrequency in enumerate(self.keyFrequency):
                if keyFrequency[1] == 0:
                    index = i
                    break
            self.keyFrequency.insert(index, [key, 0])
        else:
            self.cache_data[key] = item
            self.reorganize_items(key)

    def get(self, key):
        """
        Returns a value associated with a specific key
        """
        if key is not None and key in self.cache_data:
            self.reorganize_items(key)
        return self.cache_data.get(key, None)
        
