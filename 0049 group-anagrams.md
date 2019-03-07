---
title: LeetCode 0049group-anagrams
date: 2019-03-07 11:40:00
tags: leetcode
---

# [49] Group Anagrams

 https://leetcode.com/problems/group-anagrams/description/

 algorithms
 Medium (44.86%)
 Total Accepted:    299.1K
 Total Submissions: 666.8K
 Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'

 Given an array of strings, group anagrams together.
 
 Example:
 
 
 Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
 Output:
 [
 ⁠ ["ate","eat","tea"],
 ⁠ ["nat","tan"],
 ⁠ ["bat"]
 ]
 
 Note:
 
 
 All inputs will be in lowercase.
 The order of your output does not matter.
 
 

## Solutions:

**Python**
```python
class Solution(object):
    import collections
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def hash(s):
            index = [0] * 26
            for c in s:
                index[ord(c) - ord("a")] += 1
            return tuple(index)
        d = collections.defaultdict(list)
        for word in strs:
            d[hash(word)].append(word)
        return list(d.values())
```