---
title: LeetCode 0507perfect-number
date: 2019-03-05 10:24:31
tags: leetcode
---

# [507] Perfect Number

 https://leetcode.com/problems/perfect-number/description/

 algorithms
 Easy (33.56%)
 Total Accepted:    35.6K
 Total Submissions: 106.1K
 Testcase Example:  '28'

 We define the Perfect Number is a positive integer that is equal to the sum
 of all its positive divisors except itself. 
 
 Now, given an integer n, write a function that returns true when it is a
 perfect number and false when it is not.
 
 
 Example:
 
 Input: 28
 Output: True
 Explanation: 28 = 1 + 2 + 4 + 7 + 14
 
 

 Note:
 The input number n will not exceed 100,000,000. (1e8)
 

## Solutions:
**Python**
```python
# Time: O(sqrt(n))
# space: O(1)
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        temp = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                temp += i
                if i * i != num:  # 25 = 5 * 5, only plus 5 once
                    temp += num / i
        return temp == num
# Euler Method
```
