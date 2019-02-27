---
title: LeetCode 0066plus-one
date: 2019-02-27 14:14:17
tags: leetcode
---

# [66] Plus One

 https://leetcode.com/problems/plus-one/description/

 algorithms
 Easy (40.64%)
 Total Accepted:    352.2K
 Total Submissions: 866.4K
 Testcase Example:  '[1,2,3]'

 Given a non-empty array of digits representing a non-negative integer, plus
 one to the integer.
 
 The digits are stored such that the most significant digit is at the head of
 the list, and each element in the array contain a single digit.
 
 You may assume the integer does not contain any leading zero, except the
 number 0 itself.
 
 Example 1:
 
 
 Input: [1,2,3]
 Output: [1,2,4]
 Explanation: The array represents the integer 123.
 
 
 Example 2:
 
 
 Input: [4,3,2,1]
 Output: [4,3,2,2]
 Explanation: The array represents the integer 4321.
 
 

## Solutions:
**Python**
```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        elif digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]
```
