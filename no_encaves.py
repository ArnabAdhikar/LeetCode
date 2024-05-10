# No of Encaves
# https://www.youtube.com/watch?v=gf0zsh1FIgE&t=7s
# https://leetcode.com/problems/number-of-enclaves/description/

from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # get the dimention of the grid
        rows, cols = len(grid), len(grid[0])
        # return the no of land cells
        def dfs(r, c):
            # base case(r, c is too small or too big or visited is in water or point is already visited)
            if (r<0 or c<0 or r==rows or c==cols or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            res = 1
            # moving in 4 directions
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                res += dfs(r+dr, c+dc)
            return res
        # hash set
        visit = set()
        land, borderland = 0, 0
        # checking for total no of lands
        for r in range(rows):
            for c in range(cols):
                # calculating total no of lands
                land = land+grid[r][c]
                if ((grid[r][c]==1) and ((r,c) not in visit) and (c in [0, cols-1] or r in [0, rows-1])):
                    # only run the dfs on the border of the grid
                    borderland += dfs(r,c)
        return land-borderland
