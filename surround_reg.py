# Surround Regions
# https://www.youtube.com/watch?v=9z2BunfoZ5Y
# https://leetcode.com/problems/surrounded-regions/description/

from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            # base case
            if (r<0 or c<0 or r==rows or c==cols or board[r][c] != "O"):
                return
            # changing O-> T
            board[r][c] = "T"
            # run the dfs in 4 directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        # 1. capture the unsurrounded regions (0-> T)-> DFS
        for r in range(rows):
            for c in range(cols):
                # border cell
                if(board[r][c]=="O" and (r in [0, rows-1] or c in[0, cols-1])):
                    dfs(r,c)
        # 2. capture the surrounded regions (0-> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
        # 3. uncapture unsurrounded regions (T-> 0)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"
