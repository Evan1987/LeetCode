---
title: LeetCode 0283move-zeroes
date: 2019-03-01 11:34:39
tags: leetcode
---

# [283] Move Zeroes

 https://leetcode.com/problems/move-zeroes/description/

 algorithms
 Easy (53.59%)
 Total Accepted:    421.8K
 Total Submissions: 787.2K
 Testcase Example:  '[0,1,0,3,12]'

 Given an array nums, write a function to move all 0's to the end of it while
 maintaining the relative order of the non-zero elements.
 
 Example:
 
 
 Input: [0,1,0,3,12]
 Output: [1,3,12,0,0]
 
 Note:
 
 
 You must do this in-place without making a copy of the array.
 Minimize the total number of operations.
 

## Solutions:
**Python**
```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0  # save position of first zero
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != zero:
                    nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
```
