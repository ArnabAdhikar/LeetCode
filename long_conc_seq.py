# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/
# https://www.youtube.com/watch?v=P6RZZMu_maU

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # declaring the set
        numset = set(nums)
        longest = 0
        for i in nums:
            # check for the new sequence
            if (i-1) not in numset:
                length = 1
                # current no = n+length
                while (i+length) in numset:
                    # finding the length of the consecutive sequences
                    length+=1
                # updating the length
                longest = max(length, longest)
        return longest
