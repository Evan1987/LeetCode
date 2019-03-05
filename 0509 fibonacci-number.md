---
title: LeetCode 0509fibonacci-number
date: 2019-03-05 10:20:38
tags: leetcode
---

# [509] Fibonacci Number

 https://leetcode.com/problems/fibonacci-number/description/

 algorithms
 Easy (66.57%)
 Total Accepted:    24.5K
 Total Submissions: 36.8K
 Testcase Example:  '2'

 The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
 Fibonacci sequence, such that each number is the sum of the two preceding
 ones, starting from 0 and 1. That is,
 
 
 F(0) = 0,   F(1) = 1
 F(N) = F(N - 1) + F(N - 2), for N > 1.
 
 
 Given N, calculate F(N).
 
 
 
 Example 1:
 
 
 Input: 2
 Output: 1
 Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
 
 
 Example 2:
 
 
 Input: 3
 Output: 2
 Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
 
 
 Example 3:
 
 
 Input: 4
 Output: 3
 Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
 
 
 
 Note:
 
 0 ≤ N ≤ 30.
 

## Solutions:

**Python**
```python
# Recursive will cost much
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0 :
            return 0
        if N == 1:
            return 1

        former2 = 0
        former1 = 1
        for _ in range(2, N + 1):
            r = former1 + former2
            former2 = former1
            former1 = r
        return r
```