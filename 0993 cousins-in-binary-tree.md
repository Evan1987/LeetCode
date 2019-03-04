---
title: LeetCode 0993cousins-in-binary-tree
date: 2019-03-04 12:21:02
tags: leetcode
---

# [993] Cousins in Binary Tree

 https://leetcode.com/problems/cousins-in-binary-tree/description/

 algorithms
 Easy (53.67%)
 Total Accepted:    7.2K
 Total Submissions: 13.5K
 Testcase Example:  '[1,2,3,4]\n4\n3'

 In a binary tree, the root node is at depth 0, and children of each depth k
 node are at depth k+1.
 
 Two nodes of a binary tree are cousins if they have the same depth, but have
 different parents.
 
 We are given the root of a binary tree with unique values, and the values x
 and y of two different nodes in the tree.
 
 Return true if and only if the nodes corresponding to the values x and y are
 cousins.
 
 
 
 Example 1:
 
 
 
 Input: root = [1,2,3,4], x = 4, y = 3
 Output: false
 
 
 
 Example 2:
 
 
 
 Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
 Output: true
 
 
 
 Example 3:
 
 
 
 
 Input: root = [1,2,3,null,4], x = 2, y = 3
 Output: false
 
 
 
 
 
 Note:
 
 
 The number of nodes in the tree will be between 2 and 100.
 Each node has a unique integer value from 1 to 100.
 
 
 
 
 
 
 
 

 Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
## Solutions:
**Python**
```python
# My Solution
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val in [x, y]:
            return False
        if not root.left or not root.right:
            return False
        
        queue = [(1, root.left, root.val), (1, root.right, root.val)]
        target_depth = None
        target_parent = None
        while queue:
            depth, node, parent = queue.pop(0)
            if not target_depth:
                if node.val in [x, y]:
                    target_depth = depth
                    target_parent = parent
                else:
                    if node.left:
                        queue.append((depth + 1, node.left, node.val))
                    if node.right:
                        queue.append((depth + 1, node.right, node.val))
            else:
                if depth != target_depth:
                    return False
                elif node.val not in [x, y]:
                    continue
                else:
                    return parent != target_parent
        return False

# dfs, more space and time cost
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        parent = {}
        depth = {}

        def dfs(node, parent_val=None):
            if node:
                depth[node.val] = 1 + depth[parent_val] if parent_val else 0
                parent[node.val] = parent_val
                dfs(node.left, node.val)
                dfs(node.right, node.val)
        
        dfs(root)
        return parent[x] != parent[y] and depth[x] == depth[y]
```
