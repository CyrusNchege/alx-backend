#!/usr/bin/python3
""" MRU Cache """

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    Class MRUCache that inherits from BaseCaching
    and represents a caching system using the MRU (Most Recently Used) algorithm.
    """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache is full, remove the most recently used item.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            # Find and remove the most recently used item
            mru_key = max(self.cache_data, key=lambda k: self.cache_data[k])
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Retrieve an item from the cache.
        If the key exists, promote it as the most recently used item.
        """
        if key is not None:
            if key in self.cache_data:
                value = self.cache_data[key]
                # Promote the accessed item as the most recently used
                del self.cache_data[key]
                self.cache_data[key] = value
                return value
        return None
