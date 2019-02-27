---
title: LeetCode 0217contains-duplicate
date: 2019-02-27 14:07:49
tags: leetcode
---

# [217] Contains Duplicate

 https://leetcode.com/problems/contains-duplicate/description/

 algorithms
 Easy (50.74%)
 Total Accepted:    301.3K
 Total Submissions: 593.8K
 Testcase Example:  '[1,2,3,1]'

 Given an array of integers, find if the array contains any duplicates.
 
 Your function should return true if any value appears at least twice in the
 array, and it should return false if every element is distinct.
 
 Example 1:
 
 
 Input: [1,2,3,1]
 Output: true
 
 Example 2:
 
 
 Input: [1,2,3,4]
 Output: false
 
 Example 3:
 
 
 Input: [1,1,1,3,3,4,3,2,4,2]
 Output: true
 

## Solutions:
**Python**
```python
# Approach: Sort
# time: O(nlogn) space: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        former = None
        for x in nums:
            if x == former:
                return True
            else:
                former = x
        return False

# Approach: Hash Tables:
# time: O(n) space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for x in nums:
            if x in h:
                return True
            else:
                h.add(x)
        return False
```
