from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        # getting the dimention of the grid
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                # counting the no of fresh orranges
                if grid[r][c] == 1:
                    fresh += 1
                # identify the rotting orranges
                if grid[r][c] == 2:
                    q.append([r, c])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # q => Empty => BFS done
        while q and fresh > 0:
            # operations on rotten oranges
            for i in range(len(q)):
                r, c = q.popleft()
                # moving in the 4 directions WRT popped item
                for dr, dc in directions:
                    # current position
                    row_n, col_n = dr+r, dc+c
                    # if in bounds and fresh, make rotten
                    if (row_n< 0 or row_n==len(grid) or
                        col_n< 0 or col_n==len(grid[0]) or
                        grid[row_n][col_n] != 1):
                        continue
                    grid[row_n][col_n] = 2
                    q.append([row_n, col_n])
                    # decrement the no of fresh oranges
                    fresh -= 1
            time += 1
        if fresh == 0:
            return time
        else:
            return -1
