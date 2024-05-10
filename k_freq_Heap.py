# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
# https://www.youtube.com/watch?v=YPTqKIgVk-k

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initializing the hash map
        count = {}
        # array for storing the frequency 
        freq = [[] for i in range (len(nums)+1)]
        # counting the no of times each no occurs
        for i in nums:
            count[i] = 1+count.get(i, 0)
        # for the frequency array
        for i, j in count.items():
            freq[j].append(i)
        # result op
        res = []
        # backword traversal
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
