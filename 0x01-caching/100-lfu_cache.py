#!/usr/bin/env python3
"""
caching System
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.freq_counter = {}

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.update_frequency(key)  # Update the frequency of the key

        if len(self.cache_data) > self.MAX_ITEMS:
            self.remove_lfu()  # Remove the least frequently used item

    def get(self, key):
        if key in self.cache_data:
            self.update_frequency(key)  # Update the frequency of the accessed key
            return self.cache_data[key]
        return None

    def update_frequency(self, key):
        if key in self.freq_counter:
            self.freq_counter[key] += 1
        else:
            self.freq_counter[key] = 1

    def remove_lfu(self):
        if self.cache_data:
            min_freq = min(self.freq_counter.values())
            lfu_keys = [key for key, freq in self.freq_counter.items() if freq == min_freq]

            # If there is more than one LFU item, use LRU to decide which to remove
            if len(lfu_keys) > 1:
                lru_key = min(self.cache_data, key=lambda k: self.cache_data[k])
                lfu_keys.remove(lru_key)

            lfu_key = lfu_keys[0]
            del self.cache_data[lfu_key]
            del self.freq_counter[lfu_key]
