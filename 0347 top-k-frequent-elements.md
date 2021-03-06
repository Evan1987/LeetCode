---
title: LeetCode 0347top-k-frequent-elements
date: 2019-03-06 15:37:27
tags: leetcode
---

# [347] Top K Frequent Elements

 https://leetcode.com/problems/top-k-frequent-elements/description/

 algorithms
 Medium (53.50%)
 Total Accepted:    178K
 Total Submissions: 332.8K
 Testcase Example:  '[1,1,1,2,2,3]\n2'

 Given a non-empty array of integers, return the k most frequent elements.
 
 Example 1:
 
 
 Input: nums = [1,1,1,2,2,3], k = 2
 Output: [1,2]
 
 
 
 Example 2:
 
 
 Input: nums = [1], k = 1
 Output: [1]
 
 
 Note: 
 
 
 You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 Your algorithm's time complexity must be better than O(n log n), where n is
 the array's size.
 
 

## Solutions:

**Python**
```python
class Solution(object):
    import collections
    import heapq
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)  # O(N)
        return heapq.nlargest(k, counter.keys(),key=counter.get)  # O(NlogK)
```