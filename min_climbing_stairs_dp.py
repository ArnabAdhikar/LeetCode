# minumum cost climbing Stairs
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ
# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        # traversing the list in the reverse order(from the 3rd last element)
        for i in range(len(cost)-3,-1,-1):
            # replacing the value with the min(cost for 1 jump, 2 jump) 
            cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2])
        return min(cost[0], cost[1])
