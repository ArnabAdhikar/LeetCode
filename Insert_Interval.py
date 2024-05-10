# Insert Interval
# https://leetcode.com/problems/insert-interval/description/
# https://www.youtube.com/watch?v=A8NUOmlwOlM&t=1s

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # traversing the intervals
        for i in range(len(intervals)):
            # end value of the new interval < start value of the interval we are at
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # all the intervals comming after that will be non overlapping
                return res + intervals[i:]
            # new intervals goes after the interval we are at
            elif newInterval[0] > intervals[i][1]:
                # non overlapping
                res.append(intervals[i])
            # overlapping
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # if the 1st if statement is not executed, res array will be empty
        res.append(newInterval)
        return res
