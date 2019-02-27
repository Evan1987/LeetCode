---
title: LeetCode 0136 Single Number
date: 2019-02-27 11:33:05
tags: leetcode
---

# [136] Single Number

https://leetcode.com/problems/single-number/description/

algorithms
Easy (58.92%)
Total Accepted:    415.4K
Total Submissions: 704.9K
Testcase Example:  '[2,2,1]'

Given a non-empty array of integers, every element appears twice except for
one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?

Example 1:


Input: [2,2,1]
Output: 1


Example 2:


Input: [4,1,2,1,2]
Output: 4

## Solutions:
**Python**
```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for x in nums:
            r ^= x
        return r
```