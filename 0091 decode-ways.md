---
title: LeetCode 0091decode-ways
date: 2019-03-11 11:12:28
tags: leetcode
---

# [91] Decode Ways

 https://leetcode.com/problems/decode-ways/description/

 algorithms
 Medium (21.93%)
 Total Accepted:    240.5K
 Total Submissions: 1.1M
 Testcase Example:  '"12"'

 A message containing letters from A-Z is being encoded to numbers using the
 following mapping:
 
 
 'A' -> 1
 'B' -> 2
 ...
 'Z' -> 26
 
 
 Given a non-empty string containing only digits, determine the total number
 of ways to decode it.
 
 Example 1:
 
 
 Input: "12"
 Output: 2
 Explanation: It could be decoded as "AB" (1 2) or "L" (12).
 
 
 Example 2:
 
 
 Input: "226"
 Output: 3
 Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
 6).
 

## Solutions:

**Python**
```python
# DP
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] = dp[i - 1] if s[i] != '0'
        #        +dp[i - 2] if  "10" <= s[i - 1 : i + 1] <= "26"
        N = len(s)
        if N == 0:
            return 0
        dp = [0] * (N + 1)
        dp[0] = 1  # initial status , so dp's seq have 1 additional elements and 1 dislocation with s
        for i in range(N):
            if s[i] != "0":
                dp[i + 1] += dp[i]
            if i > 0 and "10" <= s[(i - 1) : (i + 1)] <= "26":
                dp[i + 1] += dp[i - 1]
        return dp[N]
```