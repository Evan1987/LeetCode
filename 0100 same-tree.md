---
title: LeetCode 0100same-tree
date: 2019-02-28 10:31:41
tags: leetcode
---

# [100] Same Tree

 https://leetcode.com/problems/same-tree/description/

 algorithms
 Easy (49.37%)
 Total Accepted:    348.4K
 Total Submissions: 705.6K
 Testcase Example:  '[1,2,3]\n[1,2,3]'

 Given two binary trees, write a function to check if they are the same or
 not.
 
 Two binary trees are considered the same if they are structurally identical
 and the nodes have the same value.

``` 
 Example 1:
 

 Input:    1         1
 ⁠         / \       / \
 ⁠        2   3     2   3
 
 ⁠       [1,2,3],   [1,2,3]
 
 Output: true
 
 
 Example 2:
 
 
 Input:    1         1
 ⁠         /           \
 ⁠        2             2
 
 ⁠       [1,2],     [1,null,2]
 
 Output: false
 
 
 Example 3:
 
 
 Input:    1         1
 ⁠         / \       / \
 ⁠        2   1     1   2
 
 ⁠       [1,2,1],   [1,1,2]
 
 Output: false
 
 
```
 Definition for a binary tree node.
 ```python
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
```
## Solutions:
**Python**
```python
class Solution(object):
    def isSameNode(self, p, q):
        return p.val == q.val and ((not p.left) == (not q.left)) and ((not p.right) == (not q.right))
    
    # dfs with stack
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            stack = [(p, q)]
            while stack:
                t1, t2 = stack.pop()
                if not self.isSameNode(t1, t2):
                    return False
                if t1.left:
                    stack.append((t1.left, t2.left))
                if t1.right:
                    stack.append((t1.right, t2.right))
            return True
        if not p and not q:
            return True
        return False
    
    # bfs with queue
    def isSameTree1(self, p, q):
        if p and q:
            queue = [(p, q)]
            while queue:
                t1, t2 = queue.pop(0)
                if not self.isSameNode(t1, t2):
                    return False
                if t1.left:
                    queue.append((t1.left, t2.left))
                if t1.right:
                    queue.append((t1.right, t2.right))
            return True
        if not p and not q:
            return True
        return False    
```
