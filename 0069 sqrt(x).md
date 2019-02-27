---
title: LeetCode 0069 Sqrt(x)
date: 2019-02-26 15:38:05
tags: leetcode
---

#[69] Sqrt(x)

https://leetcode.com/problems/sqrtx/description/

algorithms
Easy (30.62%)
Total Accepted:    328.5K
Total Submissions: 1.1M
Testcase Example:  '4'

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.

Since the return type is an integer, the decimal digits are truncated and
only the integer part of the result is returned.

Example 1:


Input: 4
Output: 2


Example 2:


Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
the decimal part is truncated, 2 is returned.

## Solutions:
**Python**
```python
# 手动开方法
class Solution:
    def __init__(self):
        self.one_number_mapping = self.one_number_mapping_generate()
    
    def one_number_mapping_generate(self):
        a = 1
        h = {}
        for x in range(100):
            if a * a > x:
                h[x] = a - 1
            else:
                h[x] = a
                a += 1
        return h
    
    def quick_finding(self, a, remain):
        if a != 0:
            x = int(remain / (20 * a))
            while x > 0:
                if x * (20 * a + x) <= remain:
                    break
                else:
                    x -= 1
            return x
        else:
            return self.one_number_mapping[remain]
            
    def mySqrt(self, x):
        """
        x: int
        rtype: int
        """
        sliced = []
        while x > 0:
            pop = x % 100
            sliced.append(pop)
            x //= 100
        
        r = 0
        a = 0
        remain = 0
        while len(sliced) > 0:
            remain = remain * 100 + sliced.pop()
            r_ = self.quick_finding(a, remain)
            r = r * 10 + r_
            remain -= r_ * (20 * a + r_)
            a = r
        return r
# 牛顿法
class Solution:
            
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = int((x / r + r) / 2)
        return r
```