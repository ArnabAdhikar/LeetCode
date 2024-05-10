# Triangle
# https://www.youtube.com/watch?v=OM1MTokvxs4&t=680s
# https://leetcode.com/problems/triangle/description/

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # keeping track only the bottom row
        dp = [0]*(len(triangle)+1)
        # reversed traversal of the input array
        for row in triangle[::-1]:
            # travrsing through every nos in the list
            for i,n in enumerate(row):  # n-> value; i-> index
                # finding out the min of the 2 children
                dp[i] = n+min(dp[i], dp[i+1])
        return dp[0]
