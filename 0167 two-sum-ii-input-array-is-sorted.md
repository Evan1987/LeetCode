---
title: LeetCode 0167two-sum-ii-input-array-is-sorted
date: 2019-02-27 12:35:03
tags: leetcode
---

# [167] Two Sum II - Input array is sorted

 https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

 algorithms
 Easy (49.24%)
 Total Accepted:    211.5K
 Total Submissions: 429.6K
 Testcase Example:  '[2,7,11,15]\n9'

 Given an array of integers that is already sorted in ascending order, find
 two numbers such that they add up to a specific target number.
 
 The function twoSum should return indices of the two numbers such that they
 add up to the target, where index1 must be less than index2.
 
 Note:
 
 
 Your returned answers (both index1 and index2) are not zero-based.
 You may assume that each input would have exactly one solution and you may
 not use the same element twice.
 
 
 Example:
 
 
 Input: numbers = [2,7,11,15], target = 9
 Output: [1,2]
 Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
 

## Solutions:
```python
# two pointers O(nlogn)
class Solution:
    def twoSum(self, numbers, target):
        l = 0
        h = len(numbers) - 1
        while numbers[l] + numbers[h] != target and l < h:
            if numbers[l] + numbers[h] > target:
                h -= 1
            else:
                l += 1
        return [l + 1, h + 1]
```