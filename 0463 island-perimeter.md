---
title: LeetCode 0463island-perimeter
date: 2019-03-01 12:33:43
tags: leetcode
---

# [463] Island Perimeter

 https://leetcode.com/problems/island-perimeter/description/

 algorithms
 Easy (60.26%)
 Total Accepted:    122K
 Total Submissions: 202.5K
 Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'

 You are given a map in form of a two-dimensional integer grid where 1
 represents land and 0 represents water.
 
 Grid cells are connected horizontally/vertically (not diagonally). The grid
 is completely surrounded by water, and there is exactly one island (i.e., one
 or more connected land cells).
 
 The island doesn't have "lakes" (water inside that isn't connected to the
 water around the island). One cell is a square with side length 1. The grid
 is rectangular, width and height don't exceed 100. Determine the perimeter of
 the island.
 
 
 
 Example:
 
 
 Input:
 ```
 [
    [0,1,0,0],
    ⁠[1,1,1,0],
    ⁠[0,1,0,0],
    ⁠[1,1,0,0]
 ]
 ```
 
 Output: 16
 
 Explanation: The perimeter is the 16 yellow stripes in the image below:
 
## Solutions:
**Python**
```python
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width = len(grid[0])
        length = len(grid)
        def count_water_around(x, y):
            """
            count water num around (x, y) square
            """
            l = y == 0 or grid[x][y - 1] == 0
            r = y == (width - 1) or grid[x][y + 1] == 0
            u = x == 0 or grid[x - 1][y] == 0
            d = x == (length - 1) or grid[x + 1][y] == 0
            return l + r + u + d

        return sum([count_water_around(x, y) for x in range(length) for y in range(width) if grid[x][y]])
```
