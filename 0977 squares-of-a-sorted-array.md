---
title: LeetCode 0977squares-of-a-sorted-array
date: 2019-03-01 15:36:20
tags: leetcode
---

# [977] Squares of a Sorted Array

 https://leetcode.com/problems/squares-of-a-sorted-array/description/

 algorithms
 Easy (73.16%)
 Total Accepted:    32K
 Total Submissions: 43.7K
 Testcase Example:  '[-4,-1,0,3,10]'

 Given an array of integers A sorted in non-decreasing order, return an array
 of the squares of each number, also in sorted non-decreasing order.
 
 
 
 
 Example 1:
 
 
 Input: [-4,-1,0,3,10]
 Output: [0,1,9,16,100]
 
 
 
 Example 2:
 
 
 Input: [-7,-3,2,3,11]
 Output: [4,9,9,49,121]
 
 
 
 
 Note:
 
 
 1 <= A.length <= 10000
 -10000 <= A[i] <= 10000
 A is sorted in non-decreasing order.
 
 
 
 

## Solutions:
**Python**
```python
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)        
        count = 0   # negative num
        while count < N and A[count] < 0:
            count += 1
        
        if count == N:
            return [x ** 2 for x in A][::-1]

        ans = []
        for j in range(count, N):
            while count > 0 and -A[count - 1] <= A[j]:
                ans.append(A[count - 1] ** 2)
                count -= 1
            ans.append(A[j] ** 2)
        
        # If still remain negatives
        while count > 0:
            ans.append(A[count - 1] ** 2)
            count -= 1

        return ans 
```
