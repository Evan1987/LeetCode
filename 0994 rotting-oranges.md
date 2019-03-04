---
title: LeetCode 0994rotting-oranges
date: 2019-03-04 12:52:51
tags: leetcode
---

# [994] Rotting Oranges

 https://leetcode.com/problems/rotting-oranges/description/

 algorithms
 Easy (46.45%)
 Total Accepted:    5.9K
 Total Submissions: 12.7K
 Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'

 In a given grid, each cell can have one of three values:
 
 
 the value 0 representing an empty cell;
 the value 1 representing a fresh orange;
 the value 2 representing a rotten orange.
 
 
 Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
 orange becomes rotten.
 
 Return the minimum number of minutes that must elapse until no cell has a
 fresh orange.  If this is impossible, return -1 instead.
 
 
 
 
 Example 1:
 
 
 
 
 Input: [[2,1,1],[1,1,0],[0,1,1]]
 Output: 4
 
 
 
 Example 2:
 
 
 Input: [[2,1,1],[0,1,1],[1,0,1]]
 Output: -1
 Explanation:  The orange in the bottom left corner (row 2, column 0) is never
 rotten, because rotting only happens 4-directionally.
 
 
 
 Example 3:
 
 
 Input: [[0,2]]
 Output: 0
 Explanation:  Since there are already no fresh oranges at minute 0, the
 answer is just 0.
 
 
 
 
 Note:
 
 
 1 <= grid.length <= 10
 1 <= grid[0].length <= 10
 grid[i][j] is only 0, 1, or 2.
 
 
 
 
 

## Solutions:
**Python**
```python
class Solution(object):
    import collections
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n_row, n_col = len(grid), len(grid[0])
        q = collections.deque()
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    q.append((i, j, 0))
        
        def neighbour(r, c):
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r,  c + 1)]:
                if 0 <= nr < n_row and 0 <= nc < n_col:
                    yield nr, nc

        d = 0
        while q:
            r, c, d = q.popleft()
            for nr, nc in neighbour(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, d + 1))
        
        if any(1 in row for row in grid):
            return  -1
        return d
```
