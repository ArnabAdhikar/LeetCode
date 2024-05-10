# Flood Fill

from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, p: int) -> List[List[int]]:
        # DFS
        color = image[sr][sc]
        if color == p:
            return image
        def dfs(image, sr, sc):
            image[sr][sc] = p
            directions = [[sr-1, sc],[sr+1, sc],[sr, sc+1],[sr, sc-1]]
            for r, c in directions:
                # checking the bound 
                if r>=0 and c>=0 and r<len(image) and c<len(image[0]) and image[r][c]==color:
                    dfs(image, r, c)
        dfs(image, sr, sc)
        return image
