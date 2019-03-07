---
title: LeetCode 0002add-two-numbers
date: 2019-03-07 11:37:28
tags: leetcode
---

# [2] Add Two Numbers

 https://leetcode.com/problems/add-two-numbers/description/

 algorithms
 Medium (30.62%)
 Total Accepted:    777.3K
 Total Submissions: 2.5M
 Testcase Example:  '[2,4,3]\n[5,6,4]'

 You are given two non-empty linked lists representing two non-negative
 integers. The digits are stored in reverse order and each of their nodes
 contain a single digit. Add the two numbers and return it as a linked list.
 
 You may assume the two numbers do not contain any leading zero, except the
 number 0 itself.
 
 Example:
 
 
 Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 Output: 7 -> 0 -> 8
 Explanation: 342 + 465 = 807.
 
 

 Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
## Solutions:

**Python**
```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(None)
        p, q, curr = l1, l2, ans
        carry = 0
        while p or q:
            r1 = p.val if p else 0
            r2 = q.val if q else 0
            carry, r = divmod(r1 + r2 + carry, 10)
            curr.next = ListNode(r)
            p = p.next if p else None
            q = q.next if q else None
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return ans.next 
```