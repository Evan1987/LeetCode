---
title: LeetCode 0112path-sum
date: 2019-02-28 09:36:47
tags: leetcode
---

# [112] Path Sum

 https://leetcode.com/problems/path-sum/description/

 algorithms
 Easy (36.99%)
 Total Accepted:    285.4K
 Total Submissions: 771.7K
 Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'

 Given a binary tree and a sum, determine if the tree has a root-to-leaf path
 such that adding up all the values along the path equals the given sum.
 
 Note: A leaf is a node with no children.
 
 Example:
 
 Given the below binary tree and sum = 22,
 
 ```plain
    ⁠     5
    ⁠    / \
    ⁠   4   8
    ⁠  /   / \
    ⁠ 11  13  4
    ⁠/  \      \
   7    2      1
 ```
 
 
 return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
 

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
# Recursive
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

# Depth-First-Search(DFS) and Breadth-First Search(BFS)
class Solution(object):
    
    # DFS Recursively
    def dfs(self, root, target, res):
        if root:
            if not root.left and not root.right:
                if root.val == target:
                    res.append(True)
            target -= root.val
            if root.left:
                self.dfs(root.left, target, res)
            if root.right:
                self.dfs(root.right, target, res)    
    
    # DFS Recursively
    def hasPathSum1(self, root, sum):
        res = []
        self.dfs(root, sum, res)
        return any(res)    
    
    # DFS with Stack
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        stack = [(root, root.val)]
        
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if val == sum:
                    return True
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
        return False
    
    # BFS with queue
    def hasPathSum3(self, root, sum):
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            curr, val = queue.pop(0)  # 广度优先
            if not curr.left and not curr.right:
                if val == sum:
                    return True
            if curr.left:
                queue.append((curr.left, val + curr.left.val))
            if curr.right:
                queue.append((curr.right, val + curr.right.val))
        return False

```
