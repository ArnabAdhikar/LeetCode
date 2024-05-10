# Minimum path sum
# https://www.youtube.com/watch?v=pGMsrvt0fpk
# https://leetcode.com/problems/minimum-path-sum/

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # get the dimention of the grid
        rows, cols = len(grid), len(grid[0])
        # result ans 2D grid
        res = [[float("inf")]*(cols+1) for r in range(rows+1)]
        # only one element is initialized to 0
        res[rows-1][cols] = 0
        # traversing through the grid from botton up and right to left
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                # main operation
                res[r][c] = grid[r][c]+min(res[r+1][c], res[r][c+1])
        return res[0][0]
