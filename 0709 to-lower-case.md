---
title: LeetCode 0709to-lower-case
date: 2019-03-04 19:20:59
tags: leetcode
---

# [709] To Lower Case

 https://leetcode.com/problems/to-lower-case/description/

 algorithms
 Easy (76.27%)
 Total Accepted:    76K
 Total Submissions: 99.7K
 Testcase Example:  '"Hello"'

 Implement function ToLowerCase() that has a string parameter str, and returns
 the same string in lowercase.
 
 
 
 
 Example 1:
 
 
 Input: "Hello"
 Output: "hello"
 
 
 
 Example 2:
 
 
 Input: "here"
 Output: "here"
 
 
 
 Example 3:
 
 
 Input: "LOVELY"
 Output: "lovely"
 
 
 
 
 

## Solutions:
**Python**
```python
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([chr(ord(x) + 32) if 65<=ord(x)<=90 else x for x in str])
```
