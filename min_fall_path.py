# Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/description/
# https://www.youtube.com/watch?v=b_F3mz9l-uQ

from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        cache = {}
        def dfs(r, c):
            # reached too left or right or reached end of the matrix
            if r==n:
                return 0
            if c < 0 or c==n:
                return float("inf")
            # r, c already visited
            if (r,c) in cache:
                return cache[(r, c)]
            # main recursive logic
            # return minimum path's sum
            res = matrix[r][c] + min(
                dfs(r+1, c-1),
                dfs(r+1, c),
                dfs(r+1, c+1)
            )
            cache[(r, c)] = res
            return res
        res = float("inf")
        for col in range(n):
            res = min(res, dfs(0, col))
        return res
