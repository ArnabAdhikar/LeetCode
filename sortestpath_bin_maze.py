# Shortest Path in Binary Matrix

from typing import list
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        # it is a square matrix so row = column = no
        no = len(grid)
        # keeping track of the visited with initial visited r, c
        visited = set((0,0))
        # declaring the queue(BFS) with initial value
        # r, c, length
        q = deque([(0,0,1)])
        # moement directions(8-D)
        directions = [[0,1],[1,0],[0,-1],[-1,0],
                    [1,1],[-1,-1],[1,-1],[-1,1]]
        # BFS
        while q:
            r,c,length = q.popleft()
            # checking the bound
            if min(r,c)<0 or max(r,c)>=no or grid[r][c]==1:
                continue
            # returning the length
            if r==no-1 and c==no-1:
                return length
            # movement in the 8-D
            for dr,dc in directions:
                if (dr+r,dc+c) not in visited:
                    q.append((dr+r,dc+c,length+1))
                    visited.add((dr+r,dc+c))
        return -1
