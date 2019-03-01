---
title: LeetCode 0965univalued-binary-tree
date: 2019-03-01 14:39:27
tags: leetcode
---

# [965] Univalued Binary Tree

 https://leetcode.com/problems/univalued-binary-tree/description/

 algorithms
 Easy (67.70%)
 Total Accepted:    20.1K
 Total Submissions: 29.7K
 Testcase Example:  '[1,1,1,1,1,null,1]'

 A binary tree is univalued if every node in the tree has the same value.
 
 Return true if and only if the given tree is univalued.
 
 
 
 Example 1:
 
 
 Input: [1,1,1,1,1,null,1]
 Output: true
 
 
 
 Example 2:
 
 
 Input: [2,2,2,5,2]
 Output: false
 
 
 
 
 
 Note:
 
 
 The number of nodes in the given tree will be in the range [1, 100].
 Each node's value will be an integer in the range [0, 99].
 
 

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
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        value = root.val
        queue = [root]
        while queue:
            node = queue.pop()
            if node.val != value:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True
```
