---
title: LeetCode 0009 Palindrome Number
date: 2019-02-26 15:38:05
tags: leetcode
---

# [9] Palindrome Number

https://leetcode.com/problems/palindrome-number/description/

algorithms
Easy (41.89%)
Total Accepted:    510.2K
Total Submissions: 1.2M
Testcase Example:  '121'

Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:


Input: 121
Output: true


Example 2:


Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it
becomes 121-. Therefore it is not a palindrome.


Example 3:


Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Follow up:

Coud you solve it without converting the integer to a string?

## Solutions:
**Python**
```python
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        x = str(x)
        length = len(x)
        range_ = length // 2
        if x[:range_] != x[-range_:][::-1]:
            return False
        return True

# without transforming to str
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 10 and x >= 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        
        # reverse half length of number
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10
        return x == reverted or x == reverted // 10  # in case number length is odd
```