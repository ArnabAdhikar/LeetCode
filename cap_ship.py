# Capacity To Ship Packages Within D Days
# https://www.youtube.com/watch?v=ER_oLmdc-nw
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # initialixing the left and riight bounds
        l, r = max(weights), sum(weights)
        res = r
        def canship(mid):
            # counting the no of ships
            ships = 1 
            curcap = mid  # we need atleast 1 ship
            for w in weights:
                # if the current capacity is in -ve
                if curcap-w<0:
                    # increase the no of ships and reset the current capacity
                    ships+=1
                    curcap = mid
                curcap-=w
            if ships<=days:
                return ships
        # Binary Search
        while l<=r:
            mid = (l+r)//2
            # checking if the mid capacity can be the valid capacity or not
            if canship(mid):
                # reducing the search space
                res = min(res, mid)
                # update the range
                r = mid-1
            else:
                # increase the range
                l = mid+1
        return res
