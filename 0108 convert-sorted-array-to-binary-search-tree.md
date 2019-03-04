---
title: LeetCode 0108convert-sorted-array-to-binary-search-tree
date: 2019-03-04 18:32:02
tags: leetcode
---

# [108] Convert Sorted Array to Binary Search Tree

 https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

 algorithms
 Easy (49.27%)
 Total Accepted:    238.9K
 Total Submissions: 484.8K
 Testcase Example:  '[-10,-3,0,5,9]'

 Given an array where elements are sorted in ascending order, convert it to a
 height balanced BST.
 
 For this problem, a height-balanced binary tree is defined as a binary tree
 in which the depth of the two subtrees of every node never differ by more
 than 1.
 
 Example:
 
 
 Given the sorted array: [-10,-3,0,5,9],
 
 One possible answer is: [0,-3,9,-10,null,5], which represents the following
 height balanced BST:
 
 ```
 ⁠     0
 ⁠    / \
 ⁠  -3   9
 ⁠  /   /
 ⁠-10  5
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

    def get_root(self, nums):
        index = len(nums) // 2
        return index, nums[index]

    # BST
    def sortedArrayToBST1(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        N = len(nums)
        if N == 1:
            return TreeNode(nums[0])
        
        root_index, root_val = self.get_root(nums)
        tree = TreeNode(nums[root_index])
        q = [(tree, nums[: root_index], nums[(root_index + 1): ])]
        while q:
            node, lefts, rights = q.pop(0)
            if lefts:
                index, val = self.get_root(lefts)
                node.left = TreeNode(val)
                q.append((node.left, lefts[: index], lefts[(index + 1): ]))
            if rights:
                index, val = self.get_root(rights)
                node.right = TreeNode(val)
                q.append((node.right, rights[: index], rights[(index + 1): ]))
        return tree
    
    # recursive
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[: mid])
        root.right = self.sortedArrayToBST(nums[(mid + 1): ])
        return root
```
