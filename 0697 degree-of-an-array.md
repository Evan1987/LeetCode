---
title: LeetCode 0697degree-of-an-array
date: 2019-03-04 19:43:51
tags: leetcode
---

# [697] Degree of an Array

 https://leetcode.com/problems/degree-of-an-array/description/

 algorithms
 Easy (49.17%)
 Total Accepted:    42.1K
 Total Submissions: 85.6K
 Testcase Example:  '[1,2,2,3,1]'

 Given a non-empty array of non-negative integers nums, the degree of this
 array is defined as the maximum frequency of any one of its elements.
 Your task is to find the smallest possible length of a (contiguous) subarray
 of nums, that has the same degree as nums.
 
 Example 1:
 
 Input: [1, 2, 2, 3, 1]
 Output: 2
 Explanation: 
 The input array has a degree of 2 because both elements 1 and 2 appear twice.
 Of the subarrays that have the same degree:
 [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
 The shortest length is 2. So return 2.
 
 
 
 
 Example 2:
 
 Input: [1,2,2,3,1,4,2]
 Output: 6
 
 
 
 Note:
 nums.length will be between 1 and 50,000.
 nums[i] will be an integer between 0 and 49,999.
 

## Solutions:
**Python**
```python
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        degrees = {}
        first_index = {}
        last_index = {}
        max_degree = 1

        for i, x in enumerate(nums):
            if x in degrees:
                degrees[x] += 1
                last_index[x] = i
                max_degree = max(max_degree, degrees[x])
            else:
                degrees[x] = 1
                first_index[x] = i
                last_index[x] = i
        
        summary = [
                last_index[k] - first_index[k] + 1\
                for k, degree in degrees.items() if degree == max_degree
             ]
        summary.sort()
        return summary[0]
```
