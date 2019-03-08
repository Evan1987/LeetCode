---
title: LeetCode 0739daily-temperatures
date: 2019-03-08 12:29:03
tags: leetcode
---

# [739] Daily Temperatures

 https://leetcode.com/problems/daily-temperatures/description/

 algorithms
 Medium (59.12%)
 Total Accepted:    52.1K
 Total Submissions: 88.2K
 Testcase Example:  '[73,74,75,71,69,72,76,73]'

 
 Given a list of daily temperatures T, return a list such that, for each day
 in the input, tells you how many days you would have to wait until a warmer
 temperature.  If there is no future day for which this is possible, put 0
 instead.
 
 For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
 
 
 Note:
 The length of temperatures will be in the range [1, 30000].
 Each temperature will be an integer in the range [30, 100].
 

## Solutions:

**Python**
```python
# Stack
# Time: O(N)
# Space: O(W)
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        N = len(T)
        if N == 1:
            return [0]
        
        result = [0] * N
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result
```