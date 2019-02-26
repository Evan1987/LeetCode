---
title: LeetCode 0007 Reverse-integer
date: 2019-02-26 14:57:22
tags: leetcode
---
# [7] Reverse Integer

https://leetcode.com/problems/reverse-integer/description/

algorithms
Easy (25.11%)
Total Accepted:    609K
Total Submissions: 2.4M
Testcase Example:  '123'

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:


Input: 123
Output: 321


Example 2:


Input: -123
Output: -321


Example 3:


Input: 120
Output: 21


>Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
this problem, assume that your function returns 0 when the reversed integer
overflows.


## Solutions:
**Python**
```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = int(''.join(reversed(str(abs(x)))))
        if y.bit_length() >= 32:
            return 0
        return y if x >= 0 else -y

# without transforming to str
class Solution(object):
    def __init__(self):
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31        
        self.max_thresh = int_max / 10
        self.min_thresh = int_min / 10

    def reverse(self, x):
        rev = 0
        while x != 0:
            temp = int(x / 10)  # care about floor divide and mod on negatives in python
            pop = x - temp * 10
            if (rev > self.max_thresh) or (rev == self.max_thresh and pop > 7):
                return 0
            if (rev < self.min_thresh) or (rev == self.min_thresh and pop < -8):
                return 0
            x = temp
            rev = rev * 10 + pop
        return rev

```