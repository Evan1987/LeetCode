---
title: LeetCode 0645set-mismatch
date: 2019-03-05 10:54:41
tags: leetcode
---

# [645] Set Mismatch

 https://leetcode.com/problems/set-mismatch/description/

 algorithms
 Easy (40.41%)
 Total Accepted:    42.5K
 Total Submissions: 105.3K
 Testcase Example:  '[1,2,2,4]'

 
 The set S originally contains numbers from 1 to n. But unfortunately, due to
 the data error, one of the numbers in the set got duplicated to another
 number in the set, which results in repetition of one number and loss of
 another number. 
 
 
 
 Given an array nums representing the data status of this set after the error.
 Your task is to firstly find the number occurs twice and then find the number
 that is missing. Return them in the form of an array.
 
 
 
 Example 1:
 
 Input: nums = [1,2,2,4]
 Output: [2,3]
 
 
 
 Note:
 
 The given array size will in the range [2, 10000].
 The given array's numbers won't have any order.
 
 

## Solutions:

**Python**
```python
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        expect_sum = 0
        expect_square_sum = 0
        actual_sum = 0
        actual_square_sum = 0
        for i, x in enumerate(nums):
            expect_sum += i + 1
            expect_square_sum += (i + 1) ** 2
            actual_sum += x
            actual_square_sum += x ** 2
        
        sum_diff = actual_sum - expect_sum  # dup - miss
        square_sum_diff = actual_square_sum - expect_square_sum  # dup^2 - miss^2

        dup_plus_miss = square_sum_diff / sum_diff  # dup + miss
        dup = (sum_diff + dup_plus_miss) / 2
        miss = dup_plus_miss - dup
        return [dup, miss]
```