---
title: LeetCode 0268missing-number
date: 2019-02-27 13:48:06
tags: leetcode
---

# [268] Missing Number

 https://leetcode.com/problems/missing-number/description/

 algorithms
 Easy (47.49%)
 Total Accepted:    246.4K
 Total Submissions: 518.8K
 Testcase Example:  '[3,0,1]'

 Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
 the one that is missing from the array.
 
 Example 1:
 
 
 Input: [3,0,1]
 Output: 2
 
 
 Example 2:
 
 
 Input: [9,6,4,2,3,5,7,0,1]
 Output: 8
 
 
 Note:
 Your algorithm should run in linear runtime complexity. Could you implement
 it using only constant extra space complexity?

## Solutions:
**Python**
```python
# Gauss Solution
class Solution:
    def missingNumber(self, nums):
        expected = len(nums) * (len(nums) + 1) / 2
        actual = sum(nums)
        return expected - actual
```
