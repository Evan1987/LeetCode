---
title: LeetCode 0703kth-largest-element-in-a-stream
date: 2019-03-06 12:06:36
tags: leetcode
---

# [703] Kth Largest Element in a Stream

 https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

 algorithms
 Easy (45.04%)
 Total Accepted:    23.7K
 Total Submissions: 52.5K
 Testcase Example:  '["KthLargest","add","add","add","add","add"]\n[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'

 Design a class to find the kth largest element in a stream. Note that it is
 the kth largest element in the sorted order, not the kth distinct element.
 
 Your KthLargest class will have a constructor which accepts an integer k and
 an integer array nums, which contains initial elements from the stream. For
 each call to the method KthLargest.add, return the element representing the
 kth largest element in the stream.
 
 Example:
 
 ``` java
 int k = 3;
 int[] arr = [4,5,8,2];
 KthLargest kthLargest = new KthLargest(3, arr);
 kthLargest.add(3);   // returns 4
 kthLargest.add(5);   // returns 5
 kthLargest.add(10);  // returns 5
 kthLargest.add(9);   // returns 8
 kthLargest.add(4);   // returns 8
 ```
 
 Note: 
 You may assume that nums' length ≥ k-1 and k ≥ 1.
 

 Your KthLargest object will be instantiated and called as such:
 obj = KthLargest(k, nums)
 param_1 = obj.add(val)
## Solutions:

**Python**
```python
# Time Exceed
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.q = sorted(nums)[::-1][:k]
        self.q.append(None)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        i = self.k - 1
        while val >= self.q[i] and i >= 0:
            if i == self.k - 1:
                self.q[i] = val
            else:
                self.q[i + 1], self.q[i] = self.q[i], val
            i -= 1
        return self.q[self.k - 1]

# Use Heap
class KthLargest(object):
    import heapq

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:  # 吐掉多余的元素
            heapq.heappop(self.heap)

            
    def add(self, val):
        if len(self.heap) < self.k:  # 如果堆的数量小于k则往里填值
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)  # 先push，再pop  heapreplace是先pop再push
        return self.heap[0]

```