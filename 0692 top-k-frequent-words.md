---
title: LeetCode 0692top-k-frequent-words
date: 2019-03-08 14:06:15
tags: leetcode
---

# [692] Top K Frequent Words

 https://leetcode.com/problems/top-k-frequent-words/description/

 algorithms
 Medium (44.87%)
 Total Accepted:    52.7K
 Total Submissions: 117.4K
 Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'

 Given a non-empty list of words, return the k most frequent elements.
 Your answer should be sorted by frequency from highest to lowest. If two
 words have the same frequency, then the word with the lower alphabetical
 order comes first.
 
 Example 1:
 
 Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
 Output: ["i", "love"]
 Explanation: "i" and "love" are the two most frequent words.
 ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
 
 
 
 Example 2:
 
 Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
 "is"], k = 4
 Output: ["the", "is", "sunny", "day"]
 Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
 ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
 
 
 
 Note:
 
 You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 Input words contain only lowercase letters.
 
 
 
 Follow up:
 
 Try to solve it in O(n log k) time and O(n) extra space.
 
 

## Solutions:

**Python**
```python
# Sort
# O(NlogN)
class Solution(object):
    import collections
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = collections.Counter(words)
        keys = list(counter.keys())
        keys.sort(key=lambda x: (-counter[x], x))
        return keys[:k]

# Heap
# O(klogN + N)
class Solution(object):
    import collections
    import heapq
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = collections.Counter(words)  # O(N)
        heap = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)  # O(N)
        return [heapq.heappop(heap)[1] for _ in range(k)]  # k * O(logN)
```