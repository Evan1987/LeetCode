---
title: LeetCode 0101symmetric-tree
date: 2019-02-28 11:52:53
tags: leetcode
---

# [101] Symmetric Tree

 https://leetcode.com/problems/symmetric-tree/description/

 algorithms
 Easy (42.67%)
 Total Accepted:    358.2K
 Total Submissions: 839.4K
 Testcase Example:  '[1,2,2,3,4,4,3]'

 Given a binary tree, check whether it is a mirror of itself (ie, symmetric
 around its center).
 
 
 For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
 
 ```
 ⁠   1
 ⁠  / \
 ⁠ 2   2
 ⁠/ \ / \
3  4 4  3
 ```
 
 
 But the following [1,2,2,null,3,null,3]  is not:
 ```
 ⁠   1
 ⁠  / \
 ⁠ 2   2
 ⁠  \   \
 ⁠   3   3
 ```
 
 
 
 Note:
 Bonus points if you could solve it both recursively and iteratively.
 

 Definition for a binary tree node.
 ```Python
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
    
    def isMirrorNode(self, p, q):
        return p.val == q.val and ((not p.left) == (not q.right)) and ((not p.right) == (not q.left))
    
    # BFS with queue
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if root.left and root.right:
            queue = [(root.left, root.right)]
            while queue:
                l, r = queue.pop(0)
                if not self.isMirrorNode(l, r):
                    return False
                if l.left:
                    queue.append((l.left, r.right))
                if l.right:
                    queue.append((l.right, r.left))
            return True
        
        if not root.left and not root.right:
            return True
        
        return False
```
