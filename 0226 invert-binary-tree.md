---
title: LeetCode 0226invert-binary-tree
date: 2019-03-01 12:06:15
tags: leetcode
---

# [226] Invert Binary Tree

 https://leetcode.com/problems/invert-binary-tree/description/

 algorithms
 Easy (56.98%)
 Total Accepted:    299.4K
 Total Submissions: 525.4K
 Testcase Example:  '[4,2,7,1,3,6,9]'

 Invert a binary tree.
 
 Example:
 
 Input:
 
 ```
    ⁠    4
    ⁠  /   \
    ⁠ 2     7
    ⁠/ \   / \
   1   3 6   9
 ```
 
 Output:
 
 ```
    ⁠    4
    ⁠  /   \
    ⁠ 7     2
    ⁠/ \   / \
   9   6 3   1
 ```
 Trivia:
 This problem was inspired by this original tweet by Max Howell:
 
 Google: 90% of our engineers use the software you wrote (Homebrew), but you
 can’t invert a binary tree on a whiteboard so f*** off.
 

 Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
## Solutions:
**Python**
```python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
```
