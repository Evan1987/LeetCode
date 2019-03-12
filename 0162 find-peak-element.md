---
title: LeetCode 0162find-peak-element
date: 2019-03-12 10:00:40
tags: leetcode
---

# [162] Find Peak Element

 https://leetcode.com/problems/find-peak-element/description/

 algorithms
 Medium (40.79%)
 Total Accepted:    220.1K
 Total Submissions: 539.5K
 Testcase Example:  '[1,2,3,1]'

 A peak element is an element that is greater than its neighbors.
 
 Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and
 return its index.
 
 The array may contain multiple peaks, in that case return the index to any
 one of the peaks is fine.
 
 You may imagine that nums[-1] = nums[n] = -∞.
 
 Example 1:
 
 
 Input: nums = [1,2,3,1]
 Output: 2
 Explanation: 3 is a peak element and your function should return the index
 number 2.
 
 Example 2:
 
 
 Input: nums = [1,2,1,3,5,6,4]
 Output: 1 or 5 
 Explanation: Your function can return either index number 1 where the peak
 element is 2, 
 or index number 5 where the peak element is 6.
 
 
 Note:
 
 Your solution should be in logarithmic complexity.
 

## Solutions:

**Python**
```python
# Linear Scan
# Time: O(N)
# Space: O(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        old = -float("inf")
        for i in range(len(nums)):
            now = nums[i]
            future = nums[i + 1] if i < len(nums) - 1 else -float("inf")
            if old < now and now > future:
                return i
            old = now
        return None

# Binary Scan iteratively
# Time: O(logN)
# Space: O(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:  # 意味着在 [l, mid]间一定有peak
                r = mid
            else:
                l = mid + 1  # 意味着在[mid + 1, r]间一定有peak
        return l
```