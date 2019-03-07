---
title: LeetCode 0907sum-of-subarray-minimums
date: 2019-03-07 09:42:54
tags: leetcode
---

# [907] Sum of Subarray Minimums

 https://leetcode.com/problems/sum-of-subarray-minimums/description/

 algorithms
 Medium (25.37%)
 Total Accepted:    8K
 Total Submissions: 31.4K
 Testcase Example:  '[3,1,2,4]'

 Given an array of integers A, find the sum of min(B), where B ranges over
 every (contiguous) subarray of A.
 
 Since the answer may be large, return the answer modulo 10^9 + 7.
 
 
 
 Example 1:
 
 
 Input: [3,1,2,4]
 Output: 17
 Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2],
 [1,2,4], [3,1,2,4]. 
 Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 
 
 
 Note:
 
 
 1 <= A.length <= 30000
 1 <= A[i] <= 30000
 
 
 
>主要思路：
求各个连续子集的最小值之和可以拆解为： 各元素作为最小值的子集数目 * 元素值
而各元素作为最小值的子集数目又可拆解为： 元素最小值作用域大小（左作用域 + 右作用域），子集数目 = #左作用域 * #右作用域
 

## Solutions:

**Python**
```python
# Time: O(N)
# Space: O(N)
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        N = len(A)

        # 左作用域
        # Assume A[i] is the right end of a subarray
        # Find the left-most index with which the A[i] can maintain minimum
        stack = []
        conquer_left = [None] * N
        for i in range(N):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            conquer_left[i] = stack[-1] if stack else -1
            stack.append(i)

        # 右作用域
        # Assume A[i] is the left end of a subarray
        # Find the right-most index with which the A[i] can maintain minimum
        stack = []
        conquer_right = [None] * N
        for i in range(N - 1, -1, -1):
            while stack and A[i] < A[stack[-1]]: # not have = to avoid same element cause same span
                stack.pop()
            conquer_right[i] = stack[-1] if stack else N
            stack.append(i)
        
        # with both left-conquer and right-conquer, we know the total conquer span of each element
        sum_ = sum((i - conquer_left[i]) * (conquer_right[i] - i) * A[i] for i in range(N))
        return sum_ % mod
```