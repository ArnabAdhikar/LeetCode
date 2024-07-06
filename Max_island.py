from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # base case(no DFS on water)
            if (r<0 or r==rows or c<0 or c==cols or
                grid[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r, c))
            # calculating area of the island by visiting all the 4 directions
            return (1 + dfs(r+1, c)+
                    dfs(r-1, c)+
                    dfs(r, c+1)+
                    dfs(r, c-1))
        # iterate over all the grid
        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area
