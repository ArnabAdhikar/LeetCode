# Path With Minimum Effort

import heapq
class Solution:
    def minimumEffortPath(self, heights) -> int:
        rows, cols = len(heights), len(heights[0])
        # [diff, row, col]-> initial values predefined
        minheap = [[0,0,0]]
        visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        # BFS
        while minheap:
            diff, r, c = heapq.heappop(minheap)
            # checking all the edge cases
            if (r,c) in visited:
                continue
            visited.add((r, c))
            # returning actual difference
            if (r,c) == (rows-1, cols-1):
                return diff
            # traversing in 4-D
            for dr,dc in directions:
                # current position
                new_r, new_c = r+dr, c+dc
                # checking the bound
                if (new_r<0 or new_c<0 or
                    new_r==rows or new_c==cols or
                    (new_r,new_c) in visited):
                    continue
                # difference between the neighbour position and the current position
                # and putting the maximum absolute difference
                max_diff = max(diff, abs(heights[r][c]-heights[new_r][new_c]))
                heapq.heappush(minheap,[max_diff,new_r,new_c])
