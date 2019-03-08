---
title: LeetCode 0006zig-zag-conversion
date: 2019-03-08 10:05:15
tags: leetcode
---

# [6] ZigZag Conversion

 https://leetcode.com/problems/zigzag-conversion/description/

 algorithms
 Medium (30.75%)
 Total Accepted:    290K
 Total Submissions: 943.1K
 Testcase Example:  '"PAYPALISHIRING"\n3'

 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
 of rows like this: (you may want to display this pattern in a fixed font for
 better legibility)
 
 
 P   A   H   N
 A P L S I I G
 Y   I   R
 
 
 And then read line by line: "PAHNAPLSIIGYIR"
 
 Write the code that will take a string and make this conversion given a
 number of rows:
 
 
 string convert(string s, int numRows);
 
 Example 1:
 
 
 Input: s = "PAYPALISHIRING", numRows = 3
 Output: "PAHNAPLSIIGYIR"
 
 
 Example 2:
 
 
 Input: s = "PAYPALISHIRING", numRows = 4
 Output: "PINALSIGYAHRPI"
 Explanation:
 
 P     I    N
 A   L S  I G
 Y A   H R
 P     I
 

## Solutions:

**Python**
```python
class Solution(object):

    def index_to_row(self, index, cycle):
        return min(index % cycle, cycle - index % cycle)

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        cycle = 2 * (numRows - 1)
        d = [""] * numRows
        for i, x in enumerate(s):
            row = self.index_to_row(i, cycle)
            d[row] += x
        return "".join(d)
```