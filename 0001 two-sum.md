---
title: LeetCode 0001 Two Sum
date: 2019-02-26 12:52:22
tags: leetcode
---
# [1] Two Sum

https://leetcode.com/problems/two-sum/description/

algorithms
Easy (41.64%)
Total Accepted:    1.5M
Total Submissions: 3.6M
Testcase Example:  '[2,7,11,15]'

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].

## Solutions:
**Python**
```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, x in enumerate(nums):
            expect = target - x
            if expect in h:
                return [h[expect], i]
            else:
                h[x] = i
```

