---
title: LeetCode 0976largest-perimeter-triangle
date: 2019-03-01 15:22:09
tags: leetcode
---

# [976] Largest Perimeter Triangle

 https://leetcode.com/problems/largest-perimeter-triangle/description/

 algorithms
 Easy (56.95%)
 Total Accepted:    10.1K
 Total Submissions: 17.8K
 Testcase Example:  '[2,1,2]'

 Given an array A of positive lengths, return the largest perimeter of a
 triangle with non-zero area, formed from 3 of these lengths.
 
 If it is impossible to form any triangle of non-zero area, return 0.
 
 
 
 
 
 
 
 Example 1:
 
 
 Input: [2,1,2]
 Output: 5
 
 
 
 Example 2:
 
 
 Input: [1,2,1]
 Output: 0
 
 
 
 Example 3:
 
 
 Input: [3,2,3,4]
 Output: 10
 
 
 
 Example 4:
 
 
 Input: [3,6,2,3]
 Output: 8
 
 
 
 
 Note:
 
 
 3 <= A.length <= 10000
 1 <= A[i] <= 10^6
  
 
 

## Solutions:
**Python**
```python
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        A.sort(reverse=True)
        for i in range(2, length):
            if A[i] > (A[i - 2] - A[i - 1]):
                return A[i] + A[i - 2] + A[i - 1] 
        return 0
```
