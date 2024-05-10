# Word Search
# https://leetcode.com/problems/word-search/description/

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # keeping track of all the visited cells
        path = set()
        def dfs(r, c, i):   # i= current chatacter we are at
            if i == len(word):
                return True
            # out of bounds
            if (r<0 or c<0 or
                r>=rows or c>=cols or
                word[i]!=board[r][c] or
                (r, c) in path):
                return False
            path.add((r, c))
            # traversing in all the 4 directions
            res = (dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1))
            # we have visited 4 direction from (r, c), now clean up
            path.remove((r, c))
            return res
        # traversing through all the elements in the matrix
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
