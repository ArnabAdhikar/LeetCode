# Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/
# https://www.youtube.com/watch?v=44H3cEC2fFM&t=1s

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the complete array by the start value
        intervals.sort(key = lambda i : i[0])
        # to avoid an edge cases
        output = [intervals[0]]
        for start, end in intervals[1:]:    # skipping the 1st interval as we have already added in the output
            # overlapping
            lastend = output[-1][1]
            if start <= lastend:
                # merge them
                output[-1][1] = max(lastend, end)
            else:
                # non overlapping
                output.append([start, end])
        return output
