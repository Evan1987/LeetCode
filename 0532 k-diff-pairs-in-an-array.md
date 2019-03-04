---
title: LeetCode 0532k-diff-pairs-in-an-array
date: 2019-03-04 20:05:58
tags: leetcode
---

# [532] K-diff Pairs in an Array

 https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

 algorithms
 Easy (29.36%)
 Total Accepted:    57.7K
 Total Submissions: 196.5K
 Testcase Example:  '[3,1,4,1,5]\n2'

 
 Given an array of integers and an integer k, you need to find the number of
 unique k-diff pairs in the array. Here a k-diff pair is defined as an integer
 pair (i, j), where i and j are both numbers in the array and their absolute
 difference is k.
 
 
 
 Example 1:
 
 Input: [3, 1, 4, 1, 5], k = 2
 Output: 2
 Explanation: There are two 2-diff pairs in the array, (1, 3) and (3,
 5).Although we have two 1s in the input, we should only return the number of
 unique pairs.
 
 
 
 Example 2:
 
 Input:[1, 2, 3, 4, 5], k = 1
 Output: 4
 Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
 and (4, 5).
 
 
 
 Example 3:
 
 Input: [1, 3, 1, 5, 4], k = 0
 Output: 1
 Explanation: There is one 0-diff pair in the array, (1, 1).
 
 
 
 Note:
 
 The pairs (i, j) and (j, i) count as the same pair.
 The length of the array won't exceed 10,000.
 All the integers in the given input belong to the range: [-1e7, 1e7].
 
 

## Solutions:
**Python**
```python
class Solution(object):
    import collections
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        if k == 0:
            counter = collections.Counter(nums)
            return sum(v > 1 for v in counter.values())
        if k > 0:
            return len(set(nums) & set([x + k for x in nums]))
```