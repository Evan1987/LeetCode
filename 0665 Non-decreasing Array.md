---
title: LeetCode 0665 Non-decreasing Array
date: 2019-02-26 15:38:05
tags: leetcode
---

#[665] Non-decreasing Array

https://leetcode.com/problems/non-decreasing-array/description/

algorithms
Easy (19.54%)
Total Accepted:    44K
Total Submissions: 225.5K
Testcase Example:  '[4,2,3]'


Given an array with n integers, your task is to check if it could become
non-decreasing by modifying at most 1 element.



We define an array is non-decreasing if array[i]  holds for every i (1 

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing
array.



Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one
element.



Note:
The n belongs to [1, 10,000].


## Solutions:
**Python**
```python
class Solution:
        
    def checkPossibility(self, nums):
        if len(nums) <= 2:
            return True
        modified = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modified:
                    return False
                if i >= 2 and nums[i] < nums[i - 2]:  # 关键，说明只能修改 num[i]
                    nums[i] = nums[i - 1]
                modified = True  # 修改状态
        return True

```