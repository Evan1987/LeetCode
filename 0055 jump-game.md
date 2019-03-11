---
title: LeetCode 0055jump-game
date: 2019-03-11 10:14:19
tags: leetcode
---

# [55] Jump Game

 https://leetcode.com/problems/jump-game/description/

 algorithms
 Medium (31.38%)
 Total Accepted:    239.4K
 Total Submissions: 762.9K
 Testcase Example:  '[2,3,1,1,4]'

 Given an array of non-negative integers, you are initially positioned at the
 first index of the array.
 
 Each element in the array represents your maximum jump length at that
 position.
 
 Determine if you are able to reach the last index.
 
 Example 1:
 
 
 Input: [2,3,1,1,4]
 Output: true
 Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
 
 
 Example 2:
 
 
 Input: [3,2,1,0,4]
 Output: false
 Explanation: You will always arrive at index 3 no matter what. Its
 maximum
 jump length is 0, which makes it impossible to reach the last index.
 
 

## Solutions:

**Python**
```python

# Search Forwards, easy to think out at first
# Test if the reach span forward can cover last_index
# Time: O(N)
# Space: O(1)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_index = len(nums) - 1
        max_reach = 0

        for i, max_step in enumerate(nums):
            if i > max_reach:  # the max span can't cover i, loop stop
                return False
            max_reach = max(max_reach, i + max_step)
            if max_reach >= last_index:  # the max span can cover final index, loop stop
                return True
        return True
```