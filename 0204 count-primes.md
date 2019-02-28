---
title: LeetCode 0204count-primes
date: 2019-02-28 13:53:57
tags: leetcode
---

# [204] Count Primes

 https://leetcode.com/problems/count-primes/description/

 algorithms
 Easy (28.20%)
 Total Accepted:    213.4K
 Total Submissions: 756.7K
 Testcase Example:  '10'

 Count the number of prime numbers less than a non-negative number, n.
 
 Example:
 
 
 Input: 10
 Output: 4
 Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
 

## Solutions:
**Python**
```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        primes = [1] * n
        primes[0] = primes[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i : n : i] = [0] * len(range(i * i, n, i))
        return sum(primes)
```
