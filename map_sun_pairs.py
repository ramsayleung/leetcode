"""
source: https://leetcode.com/problems/map-sum-pairs/
author: Ramsay Leung
date: 2020-02-21

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:

Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""

# I know trie is perfectly suitable for this case, but dict is so handy that if I want to use trie
# I need to build a trie by myself. So, dict is great.

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def insert(self, key: str, val: int) -> None:
        self.data[key] = val

    def sum(self, prefix: str) -> int:
        sum = 0
        for key, value in self.data.items():
            if key.startswith(prefix):
                sum += value
        return sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
