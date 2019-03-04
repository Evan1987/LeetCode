---
title: LeetCode 0796rotate-string
date: 2019-03-04 15:38:29
tags: leetcode
---

# [796] Rotate String

 https://leetcode.com/problems/rotate-string/description/

 algorithms
 Easy (48.75%)
 Total Accepted:    33.8K
 Total Submissions: 69.3K
 Testcase Example:  '"abcde"\n"cdeab"'

 We are given two strings, A and B.
 
 A shift on A consists of taking string A and moving the leftmost character to
 the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
 after one shift on A. Return True if and only if A can become B after some
 number of shifts on A.
 
 
 Example 1:
 Input: A = 'abcde', B = 'cdeab'
 Output: true
 
 Example 2:
 Input: A = 'abcde', B = 'abced'
 Output: false
 
 
 Note:
 
 
 A and B will have length at most 100.
 
 

## Solutions:
**Python**
```python
# O(n2)
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        return B in (A + A)
# kmp
```
