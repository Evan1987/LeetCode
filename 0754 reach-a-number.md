---
title: LeetCode 0754reach-a-number
date: 2019-03-18 20:03:16
tags: leetcode
---

# [754] Reach a Number

 https://leetcode.com/problems/reach-a-number/description/

 algorithms
 Easy (31.81%)
 Total Accepted:    8.8K
 Total Submissions: 27.6K
 Testcase Example:  '1'

 
 You are standing at position 0 on an infinite number line.  There is a goal
 at position target.
 
 On each move, you can either go left or right.  During the n-th move
 (starting from 1), you take n steps.
 
 Return the minimum number of steps required to reach the destination.
 
 
 Example 1:
 
 Input: target = 3
 Output: 2
 Explanation:
 On the first move we step from 0 to 1.
 On the second step we step from 1 to 3.
 
 
 
 Example 2:
 
 Input: target = 2
 Output: 3
 Explanation:
 On the first move we step from 0 to 1.
 On the second move we step  from 1 to -1.
 On the third move we step from -1 to 2.
 
 
 
 Note:
 target will be a non-zero integer in the range [-10^9, 10^9].
 

## Solutions:

**Python**
```python
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = target if target > 0 else -target
        k = 0
        total = 0
        while total < target:
            k += 1
            total += k
        
        delta = total - target
        # if delta == 0:
        #     return k
        # if delta % 2 == 0:
        #     return k
        # if delta % 2 == 1:
        #     return k + 1 if (k + 1) % 2 else k + 2
        
        return k if delta % 2 == 0 else k + 1 + k % 2
```