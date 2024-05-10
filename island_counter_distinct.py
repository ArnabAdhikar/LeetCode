# distinct island count
"""
Created on Sat Feb  3 20:24:07 2024

@author: ARNAB ADHIKARY
"""

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    # DFS
    def dfs(self,row,col,visited,grid,a,row0,col0):
        n=len(grid)
        m=len(grid[0])
        visited[row][col]=1
        # storing (coordinate-base)
        a.append(((row-row0),(col-col0)))
        # traversal in all the 4 directions
        row_direction = [-1,0,1,0]
        col_direction = [0,1,0,-1]
        for i in range(4):
            nrow = row + row_direction[i]
            ncol = col + col_direction[i]
            if nrow>=0 and n > nrow and ncol >=0 and m > ncol and visited[nrow][ncol]==0 and grid[nrow][ncol]==1:
                self.dfs(nrow,ncol,visited,grid,a,row0,col0)
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n=len(grid)
        m=len(grid[0])
        visited=[[0]*m for _ in range(n)]
        st=set()
        
        for i in range(n):
            for j in range(m):
                if visited[i][j]==0 and grid[i][j]==1:
                    a=[]
                    self.dfs(i,j,visited,grid,a,i,j)
                    st.add(tuple(a))
                    
        return len(st) 
