---
title: LeetCode 0075sort-colors
date: 2019-03-11 12:02:32
tags: leetcode
---

# [75] Sort Colors

 https://leetcode.com/problems/sort-colors/description/

 algorithms
 Medium (41.41%)
 Total Accepted:    294.7K
 Total Submissions: 711.8K
 Testcase Example:  '[2,0,2,1,1,0]'

 Given an array with n objects colored red, white or blue, sort them in-place
 so that objects of the same color are adjacent, with the colors in the order
 red, white and blue.
 
 Here, we will use the integers 0, 1, and 2 to represent the color red, white,
 and blue respectively.
 
 Note: You are not suppose to use the library's sort function for this
 problem.
 
 Example:
 
 
 Input: [2,0,2,1,1,0]
 Output: [0,0,1,1,2,2]
 
 Follow up:
 
 
 A rather straight forward solution is a two-pass algorithm using counting
 sort.
 First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
 array with total number of 0's, then 1's and followed by 2's.
 Could you come up with a one-pass algorithm using only constant space?
 
 

## Solutions:

**Python**
```python
# Lomuto
class Solution(object):
    # partition sort
    # [0, i), [i, j), [j, N) are 0s, 1s and 2s sorted in place for [0, N)
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = j = 0  # two partitioner
        for k in range(N):
            v = nums[k]
            nums[k] = 2  # 2 for [0, N)
            if v < 2:
                nums[j] = 1  # 1 for [0, j)
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1  # 0 for [0, i)
    
    # [0, i), [i, j), [j, k), [k, N) are 0s, 1s, 2s and 3s
    def sortColors2(self, nums):
        """
        :type nums: List[Int], enum 0, 1, 2, 3
        """
        N = len(nums)
        i = j = k = 0   # three partitioner
        for t in range(N):
            v = nums[t]
            nums[t] = 3  # 3 for [0, N)
            if v < 3:
                nums[k] = 2  # 2 for [0, k)
                k += 1
            if v < 2:
                nums[j] = 1  # 1 for [0, j)
                j += 1
            if v == 0:
                nums[i] = 0  # 0 for [0, i)
                i += 1
```