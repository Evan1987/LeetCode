---
title: LeetCode 0506relative-ranks
date: 2019-03-05 10:43:23
tags: leetcode
---

# [506] Relative Ranks

 https://leetcode.com/problems/relative-ranks/description/

 algorithms
 Easy (47.91%)
 Total Accepted:    39.8K
 Total Submissions: 83K
 Testcase Example:  '[5,4,3,2,1]'

 
 Given scores of N athletes, find their relative ranks and the people with the
 top three highest scores, who will be awarded medals: "Gold Medal", "Silver
 Medal" and "Bronze Medal".
 
 Example 1:
 
 Input: [5, 4, 3, 2, 1]
 Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
 Explanation: The first three athletes got the top three highest scores, so
 they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two
 athletes, you just need to output their relative ranks according to their
 scores.
 
 
 
 Note:
 
 N is a positive integer and won't exceed 10,000.
 All the scores of athletes are guaranteed to be unique.
 
 
 

## Solutions:

**Python**
```python
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def prize(rank):
            if rank == 0:
                return "Gold Medal"
            if rank == 1:
                return "Silver Medal"
            if rank == 2:
                return "Bronze Medal"
            return str(rank + 1)
        score_rank = {k:  prize(i) for i, k in enumerate(sorted(nums)[::-1])}
        
        return [score_rank[score] for score in nums]
```