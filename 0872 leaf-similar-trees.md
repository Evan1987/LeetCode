---
title: LeetCode 0872leaf-similar-trees
date: 2019-03-01 15:09:46
tags: leetcode
---

# [872] Leaf-Similar Trees

 https://leetcode.com/problems/leaf-similar-trees/description/

 algorithms
 Easy (62.17%)
 Total Accepted:    34.9K
 Total Submissions: 56.2K
 Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'

 Consider all the leaves of a binary tree.  From left to right order, the
 values of those leaves form a leaf value sequence.

 ![Alt text](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)
 
 For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
 8).
 
 Two binary trees are considered leaf-similar if their leaf value sequence is
 the same.
 
 Return true if and only if the two given trees with head nodes root1 and
 root2 are leaf-similar.
 
 
 
 Note:
 
 
 Both of the given trees will have between 1 and 100 nodes.
 
 

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

# dfs
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
```
