---
title: LeetCode 0661image-smoother
date: 2019-03-06 14:04:36
tags: leetcode
---

# [661] Image Smoother

 https://leetcode.com/problems/image-smoother/description/

 algorithms
 Easy (47.93%)
 Total Accepted:    31.5K
 Total Submissions: 65.7K
 Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'

 Given a 2D integer matrix M representing the gray scale of an image, you need
 to design a smoother to make the gray scale of each cell becomes the average
 gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
 cell has less than 8 surrounding cells, then use as many as you can.
 
 Example 1:
 
 Input:
 [[1,1,1],
 ⁠[1,0,1],
 ⁠[1,1,1]]
 Output:
 [[0, 0, 0],
 ⁠[0, 0, 0],
 ⁠[0, 0, 0]]
 Explanation:
 For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
 For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
 For the point (1,1): floor(8/9) = floor(0.88888889) = 0
 
 
 
 Note:
 
 The value in the given matrix is in the range of [0, 255].
 The length and width of the given matrix are in the range of [1, 150].
 
 

## Solutions:

**Python**
```python
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        height = len(M)
        width = len(M[0])
        ans = [[0] * width for _ in range(height)]

        for r in range(height):
            for c in range(width):
                count = 0
                for nr in (r - 1, r, r + 1):
                    for nc in (c - 1, c, c + 1):
                        if 0 <= nr < height and 0 <= nc < width:
                            count += 1
                            ans[r][c] += M[nr][nc]
                ans[r][c] //= count
        return ans
```