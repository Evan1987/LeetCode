---
title: LeetCode 0111minimum-depth-of-binary-tree
date: 2019-03-04 14:46:58
tags: leetcode
---

# [111] Minimum Depth of Binary Tree

 https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

 algorithms
 Easy (34.85%)
 Total Accepted:    274.5K
 Total Submissions: 787.5K
 Testcase Example:  '[3,9,20,null,null,15,7]'

 Given a binary tree, find its minimum depth.
 
 The minimum depth is the number of nodes along the shortest path from the
 root node down to the nearest leaf node.
 
 Note: A leaf is a node with no children.
 
 Example:
 
 Given binary tree [3,9,20,null,null,15,7],
 
 ```
 ⁠   3
 ⁠  / \
 ⁠ 9  20
 ⁠   /  \
 ⁠  15   7
 ```
 return its minimum depth = 2.
 

 Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
## Solutions:
**Python**
```python
# BFS
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        q = [(1, root)]
        min_depth = float("inf")
        while q:
            depth, node = q.pop(0)
            if depth > min_depth:
                return min_depth
            if not node.left and not node.right:
                min_depth = depth if depth < min_depth else min_depth
            else:
                if node.left:
                    q.append((depth + 1, node.left))
                if node.right:
                    q.append((depth + 1, node.right))

        return min_depth    
```
