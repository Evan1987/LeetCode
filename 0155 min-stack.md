---
title: LeetCode 0155min-stack
date: 2019-03-06 14:58:36
tags: leetcode
---

# [155] Min Stack

 https://leetcode.com/problems/min-stack/description/

 algorithms
 Easy (35.70%)
 Total Accepted:    270.8K
 Total Submissions: 758.5K
 Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'

 
 Design a stack that supports push, pop, top, and retrieving the minimum
 element in constant time.
 
 
 push(x) -- Push element x onto stack.
 
 
 pop() -- Removes the element on top of the stack.
 
 
 top() -- Get the top element.
 
 
 getMin() -- Retrieve the minimum element in the stack.
 
 
 
 
 Example:
 
 MinStack minStack = new MinStack();
 minStack.push(-2);
 minStack.push(0);
 minStack.push(-3);
 minStack.getMin();   --> Returns -3.
 minStack.pop();
 minStack.top();      --> Returns 0.
 minStack.getMin();   --> Returns -2.
 
 

 Your MinStack object will be instantiated and called as such:
 obj = MinStack()
 obj.push(x)
 obj.pop()
 param_3 = obj.top()
 param_4 = obj.getMin()
## Solutions:

**Python**
```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.s:
            del self.s[-1]

    def top(self):
        """
        :rtype: int
        """
        if self.s:
            return self.s[-1]
        return None
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.s)
```