# Non-overlapping Intervals
# https://www.youtube.com/watch?v=nONCGxWoUfM
# https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sorting the array
        intervals.sort()
        res = 0
        # keeping track of the first's end value
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            # not overlapping
            if start>=prevend:
                prevend = end
            # overlapping
            else:
                # removing 1 of the intervals
                res += 1
                # keep the interval with minimum end value
                prevend = min(end, prevend)
        return res
