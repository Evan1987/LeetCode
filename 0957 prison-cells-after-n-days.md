---
title: LeetCode 0957prison-cells-after-n-days
date: 2019-03-06 17:01:46
tags: leetcode
---

# [957] Prison Cells After N Days

 https://leetcode.com/problems/prison-cells-after-n-days/description/

 algorithms
 Medium (38.01%)
 Total Accepted:    6.1K
 Total Submissions: 16.1K
 Testcase Example:  '[0,1,0,1,1,0,0,1]\n7'

 There are 8 prison cells in a row, and each cell is either occupied or
 vacant.
 
 Each day, whether the cell is occupied or vacant changes according to the
 following rules:
 
 
 If a cell has two adjacent neighbors that are both occupied or both vacant,
 then the cell becomes occupied.
 Otherwise, it becomes vacant.
 
 
 (Note that because the prison is a row, the first and the last cells in the
 row can't have two adjacent neighbors.)
 
 We describe the current state of the prison in the following way: cells[i] ==
 1 if the i-th cell is occupied, else cells[i] == 0.
 
 Given the initial state of the prison, return the state of the prison after N
 days (and N such changes described above.)
 
 
 
 
 
 
 
 
 
 Example 1:
 
 
 Input: cells = [0,1,0,1,1,0,0,1], N = 7
 Output: [0,0,1,1,0,0,0,0]
 Explanation: 
 The following table summarizes the state of the prison on each day:
 Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
 Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
 Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
 Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
 Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
 Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
 Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
 Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
 
 
 
 
 Example 2:
 
 
 Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
 Output: [0,0,1,1,1,1,1,0]
 
 
 
 
 Note:
 
 
 cells.length == 8
 cells[i] is in {0, 1}
 1 <= N <= 10^9
 
 
 

## Solutions:

**Python**
```python
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def nextDay(cells):
            return [int(i > 0 and i < 7 and cells[i - 1] == cells[i + 1]) for i in range(8)]
        
        if N == 0:
            return cells

        seen = {}
        i = 0
        while True:
            c = tuple(cells)
            if c in seen:
                start = seen[c]
                break
            if i == N:
                return cells
            seen[c] = i
            cells = nextDay(cells)
            i += 1
        # when break (i-start) is the loop length of cell transformation
        N = start + (N - start) % (i - start)
        seen = {dayNum: c for c, dayNum in seen.items()}
        return list(seen[N])
```