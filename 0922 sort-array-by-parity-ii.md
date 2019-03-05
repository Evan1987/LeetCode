---
title: LeetCode 0922sort-array-by-parity-ii
date: 2019-03-05 09:43:09
tags: leetcode
---

# [922] Sort Array By Parity II

 https://leetcode.com/problems/sort-array-by-parity-ii/description/

 algorithms
 Easy (66.73%)
 Total Accepted:    29.9K
 Total Submissions: 44.7K
 Testcase Example:  '[4,2,5,7]'

 Given an array A of non-negative integers, half of the integers in A are odd,
 and half of the integers are even.
 
 Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is
 even, i is even.
 
 You may return any answer array that satisfies this condition.
 
 
 
 Example 1:
 
 
 Input: [4,2,5,7]
 Output: [4,5,2,7]
 Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been
 accepted.
 
 
 
 
 Note:
 
 
 2 <= A.length <= 20000
 A.length % 2 == 0
 0 <= A[i] <= 1000
 

## Solutions:
**Python**
```python

# Time: O(N)
# Space: O(N)
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = [None] * len(A)
        even_index = 0
        odd_index = 1
        for i, x in enumerate(A):
            if x % 2 == 0:  # even
                ans[even_index] = x
                even_index += 2
            else:  # odd
                ans[odd_index] = x
                odd_index += 2
        return ans

# inplace transform
# Time: O(N)
# Space: O(1)
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1  # odd index
        for i in range(0, len(A), 2):  # loop even index
            if A[i] % 2:  # odd
                while A[j] % 2:  # odd index with odd integer, no movement
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
```
