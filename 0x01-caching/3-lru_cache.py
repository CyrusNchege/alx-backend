#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the LRUCache
        """
        super().__init__()
        self.lru_order = []  # Maintain order of keys to track LRU

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find and remove the least recently used item (the first in the order list)
                lru_key = self.lru_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.lru_order.append(key)

    def get(self, key):
        """ Get an item by key and update its position in the LRU order
        """
        if key is not None:
            value = self.cache_data.get(key)
            if value:
                self.lru_order.remove(key)
                self.lru_order.append(key)
            return value
