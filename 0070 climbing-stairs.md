---
title: LeetCode 0070climbing-stairs
date: 2019-03-01 17:51:58
tags: leetcode
---

# [70] Climbing Stairs

 https://leetcode.com/problems/climbing-stairs/description/

 algorithms
 Easy (43.40%)
 Total Accepted:    356.4K
 Total Submissions: 821.2K
 Testcase Example:  '2'

 You are climbing a stair case. It takes n steps to reach to the top.
 
 Each time you can either climb 1 or 2 steps. In how many distinct ways can
 you climb to the top?
 
 Note: Given n will be a positive integer.
 
 Example 1:
 
 
 Input: 2
 Output: 2
 Explanation: There are two ways to climb to the top.
 1. 1 step + 1 step
 2. 2 steps
 
 
 Example 2:
 
 
 Input: 3
 Output: 3
 Explanation: There are three ways to climb to the top.
 1. 1 step + 1 step + 1 step
 2. 1 step + 2 steps
 3. 2 steps + 1 step
 
 

## Solutions:
**Python**
```python
class Solution(object):
    # Approach 1: Brute Force (very expensive)
    # Time: O(2^n)
    # Space: O(n)
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
    # Approach 2: Dynamic Programming
    # Time: O(n)
    # Space: O(n)
    def climbStairs2(self, n):
        d = [0] * (n + 1)
        for i in range(n + 1):
            if i <= 1:
                d[i] = 1
            else:
                # Recursive formula
                d[i] = d[i - 1] + d[i - 2]
        return d[n]
    
    # Approach 3: Recursion with memoization
    # Time: O(n)
    # Space: O(n)
    def climbStairs3(self, n):
        def f(i, n, mem):
            if i > n:
                return 0
            if i == n:
                return 1
            if mem[i] > 0:
                return mem[i]
            mem[i] = f(i + 1, n, mem) + f(i + 2, n, mem)
            return mem[i]

        mem = [0] * (n + 1)
        return f(0, n, mem)
```
