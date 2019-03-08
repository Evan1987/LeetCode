---
title: LeetCode 0677map-sum-pairs
date: 2019-03-08 14:18:19
tags: leetcode
---

# [677] Map Sum Pairs

 https://leetcode.com/problems/map-sum-pairs/description/

 algorithms
 Medium (51.18%)
 Total Accepted:    23.2K
 Total Submissions: 45.3K
 Testcase Example:  '["MapSum", "insert", "sum", "insert", "sum"]\n[[], ["apple",3], ["ap"], ["app",2], ["ap"]]'

 
 Implement a MapSum class with insert, and sum methods.
 
 
 
 For the method insert, you'll be given a pair of (string, integer). The
 string represents the key and the integer represents the value. If the key
 already existed, then the original key-value pair will be overridden to the
 new one.
 
 
 
 For the method sum, you'll be given a string representing the prefix, and you
 need to return the sum of all the pairs' value whose key starts with the
 prefix.
 
 
 Example 1:
 
 Input: insert("apple", 3), Output: Null
 Input: sum("ap"), Output: 3
 Input: insert("app", 2), Output: Null
 Input: sum("ap"), Output: 5
 
 
 

 Your MapSum object will be instantiated and called as such:
 obj = MapSum()
 obj.insert(key,val)
 param_2 = obj.sum(prefix)
## Solutions:

**Python**
```python
# Brute
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def insert(self, key, val):  # O(1)
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.d[key] = val
        

    def sum(self, prefix):  # O(N * P)  ==> key[:p] => O(p)
        """
        :type prefix: str
        :rtype: int
        """
        l = len(prefix)
        valid = [val for key, val in self.d.items() if key[:l] == prefix]
        return sum(valid) if valid else 0

# prefix hashmap
class MapSum(object):
    import collections
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.score = collections.defaultdict(int)
        

    def insert(self, key, val):  # O(K^2)
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        delta = val - self.d.get(key, 0)
        self.d[key] = val

        for i in range(len(key) + 1):
            self.score[key[:i]] += delta
        

    def sum(self, prefix):  # O(1)
        """
        :type prefix: str
        :rtype: int
        """
        return self.score[prefix]


# Trie
class TrieNode(object):
    __slots__ = ["children", "score"]
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.root = TrieNode()
        

    def insert(self, key, val):  # O(K)
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta       
        

    def sum(self, prefix):  # O(K)
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score
```