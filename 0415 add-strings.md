---
title: LeetCode 0415add-strings
date: 2019-02-28 14:40:18
tags: leetcode
---

# [415] Add Strings

 https://leetcode.com/problems/add-strings/description/

 algorithms
 Easy (43.01%)
 Total Accepted:    84.2K
 Total Submissions: 195.7K
 Testcase Example:  '"0"\n"0"'

 Given two non-negative integers num1 and num2 represented as string, return
 the sum of num1 and num2.
 
 Note:
 
 The length of both num1 and num2 is < 5100.
 Both num1 and num2 contains only digits 0-9.
 Both num1 and num2 does not contain any leading zero.
 You must not use any built-in BigInteger library or convert the inputs to
 integer directly.
 
 

## Solutions:
**Python**
```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ""
        n1 = list(num1)
        n2 = list(num2)
        l1 = len(n1)
        l2 = len(n2)
        next_ = 0
        while (n1 or n2):
            x = int(n1.pop()) if l1 > 0 else 0
            y = int(n2.pop()) if l2 > 0 else 0
            l1 -= 1
            l2 -= 1
            sum_ = x + y + next_
            if sum_ >= 10:
                target = sum_ - 10
                next_ = 1
            else:
                target = sum_
                next_ = 0
            result = str(target) + result
        
        if next_ == 1:
            result = "1" + result
        return result
```
