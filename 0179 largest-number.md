---
title: LeetCode 0179largest-number
date: 2019-03-12 10:56:21
tags: leetcode
---

# [179] Largest Number

 https://leetcode.com/problems/largest-number/description/

 algorithms
 Medium (25.30%)
 Total Accepted:    121.6K
 Total Submissions: 480.6K
 Testcase Example:  '[10,2]'

 Given a list of non negative integers, arrange them such that they form the
 largest number.
 
 Example 1:
 
 
 Input: [10,2]
 Output: "210"
 
 Example 2:
 
 
 Input: [3,30,34,5,9]
 Output: "9534330"
 
 
 Note: The result may be very large, so you need to return a string instead of
 an integer.
 

## Solutions:

**Python**
```python
class Largest(str):
    def __lt__(a, b):  # 判断a是否小于b（a是否排在前面）
        return a + b > b + a

class Solution(object):
    import functools
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # def compare(x, y):
        #     if x + y < y + x:  # x应该在后面
        #         return 1  # 认为 x > y 这样 x 就在后面了
        #     else:
        #         return -1
        # r = "".join(sorted(map(str, nums), functools.cmp_to_key(compare)))
        r = "".join(sorted(map(str, nums), key=Largest))
        return "0" if r[0] == "0" else r
```