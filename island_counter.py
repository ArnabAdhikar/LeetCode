# https://leetcode.com/problems/number-of-islands/description/

from collections import deque
class Solution:
    # DFS
    def numIslands(self, grid) -> int:
        out = 0
        n_rows, n_cols = len(grid), len(grid[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1":
                    out += 1
                    # traverse subgraph for island, for very neighbouring 1 make it 0 and continue the traversal
                    # coordinates are appended
                    stack = deque([(r, c)])
                    while stack:
                        r0, c0 = stack.pop()
                        # checking for the neighbouring blocks
                        if 0 <= r0 < n_rows and 0 <= c0 < n_cols and grid[r0][c0] == "1":
                            grid[r0][c0] = "0"
                            # push the node after traversal in 4 directions
                            for rd, cd in dirs:
                                stack.append((r0 + rd, c0 + cd))
        return out
