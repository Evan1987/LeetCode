---
title: LeetCode 0231power-of-two
date: 2019-02-27 19:50:08
tags: leetcode
---

# [231] Power of Two

 https://leetcode.com/problems/power-of-two/description/

 algorithms
 Easy (41.61%)
 Total Accepted:    212.6K
 Total Submissions: 511K
 Testcase Example:  '1'

 Given an integer, write a function to determine if it is a power of two.
 
 Example 1:
 
 
 Input: 1
 Output: true 
 Explanation: 20 = 1
 
 
 Example 2:
 
 
 Input: 16
 Output: true
 Explanation: 24 = 16
 
 Example 3:
 
 
 Input: 218
 Output: false
 

## Solutions:
**Python**
```python
# 常规解法
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if n == 1:
            return True
        r = 0
        while r == 0:
            if n == 2:
                return True
            r = n % 2
            n /= 2
            
        return False
# 位运算
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n - 1))
```
