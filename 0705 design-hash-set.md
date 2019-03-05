---
title: LeetCode 0705design-hash-set
date: 2019-03-05 11:10:44
tags: leetcode
---

# [705] Design HashSet

 https://leetcode.com/problems/design-hashset/description/

 algorithms
 Easy (50.59%)
 Total Accepted:    15.1K
 Total Submissions: 29.8K
 Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n[[],[1],[2],[1],[3],[2],[2],[2],[2]]'

 Design a HashSet without using any built-in hash table libraries.
 
 To be specific, your design should include these functions:
 
 
 add(value): Insert a value into the HashSet. 
 contains(value) : Return whether the value exists in the HashSet or not.
 remove(value): Remove a value in the HashSet. If the value does not exist in
 the HashSet, do nothing.
 
 
 
 Example:
 
 
 MyHashSet hashSet = new MyHashSet();
 hashSet.add(1);         
 hashSet.add(2);         
 hashSet.contains(1);    // returns true
 hashSet.contains(3);    // returns false (not found)
 hashSet.add(2);          
 hashSet.contains(2);    // returns true
 hashSet.remove(2);          
 hashSet.contains(2);    // returns false (already removed)
 
 
 
 Note:
 
 
 All values will be in the range of [0, 1000000].
 The number of operations will be in the range of [1, 10000].
 Please do not use the built-in HashSet library.
 
 

 Your MyHashSet object will be instantiated and called as such:
 obj = MyHashSet()
 obj.add(key)
 obj.remove(key)
 param_3 = obj.contains(key)
## Solutions:

**Python**
```python
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = [None] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.s[key] = 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.s[key] = None
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.s[key] is not None
```