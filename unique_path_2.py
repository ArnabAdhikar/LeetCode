# unique path II
# https://www.youtube.com/watch?v=d3UOz7zdE4I&t=1s
# https://leetcode.com/problems/unique-paths-ii/description/

from typing import List
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # initializing the grid (m-> ROWS)
        m, n = len(grid), len(grid[0])
        # space allocated for storing last row's result
        dp = [0]*n
        # last value is set to 1
        dp[n-1] = 1
        # traversing the list of rows in reversed order
        for r in reversed(range(m)):
            # traversing the list of columns in reversed order
            for c in reversed(range(n)):
                # obstacle
                if grid[r][c]==1:
                    dp[c] = 0
                # if column is in bound
                elif c+1<n:
                    # main op(inplace)
                    dp[c] = dp[c]+dp[c+1]   # dp[c]-> bottom value, dp[c+1]-> Right Value
                # if column is out of bound
                else:
                    dp[c] = dp[c]+0
        return dp[0]
