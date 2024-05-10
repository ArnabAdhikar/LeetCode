# Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# https://www.youtube.com/watch?v=s-VkcjHqkGI

from typing import List
class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        # get the dimention of the grid
        rows, cols = len(height), len(height[0])
        # hash set for pacific and atlantic
        pac, atl = set(), set()

        def dfs(r, c, visit, prevheight):
            # if the co-ordinate is already been visited or it's out of bound
            if ((r, c) in visit or 
                r<0 or c<0 or r==rows or c==cols or
                height[r][c] < prevheight):  # height is too small
                return
            # after visiting
            visit.add((r, c))
            # run DFS in all the 4 directions
            dfs(r+1, c, visit, height[r][c])
            dfs(r-1, c, visit, height[r][c])
            dfs(r, c+1, visit, height[r][c])
            dfs(r, c-1, visit, height[r][c])
            

        # first row=> Pacific ocean
        for c in range(cols):
            # from ocean to the cell
            dfs(0, c, pac, height[0][c])
            # last row=> Atlantic ocean
            dfs(rows-1, c, atl, height[rows-1][c])
        # first column=> Pacific ocean
        for r in range(rows):
            # from ocean to the cell
            dfs(r, 0, pac, height[r][0])
            # last column=> Atlantic ocean
            dfs(r, cols-1, atl, height[r][cols-1])
        
        # After marking all the grid
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
