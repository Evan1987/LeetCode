---
title: LeetCode 0867transpose-matrix
date: 2019-03-18 19:41:02
tags: leetcode
---

# [867] Transpose Matrix

 https://leetcode.com/problems/transpose-matrix/description/

 algorithms
 Easy (63.75%)
 Total Accepted:    39.1K
 Total Submissions: 61.3K
 Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'

 Given a matrix A, return the transpose of A.
 
 The transpose of a matrix is the matrix flipped over it's main diagonal,
 switching the row and column indices of the matrix.
 
 
 
 
 Example 1:
 
 
 Input: [[1,2,3],[4,5,6],[7,8,9]]
 Output: [[1,4,7],[2,5,8],[3,6,9]]
 
 
 
 Example 2:
 
 
 Input: [[1,2,3],[4,5,6]]
 Output: [[1,4],[2,5],[3,6]]
 
 
 
 
 Note:
 
 
 1 <= A.length <= 1000
 1 <= A[0].length <= 1000
 
 
 
 

## Solutions:

**Python**
```python
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n_row = len(A)
        n_col = len(A[0])
        res = [[None] * n_row for _ in range(n_col)]
        for i, row in enumerate(A):
            for j, ele in enumerate(A[i]):
                res[j][i] = ele
        return res
```