# rotten oranges

from collections import deque
def minTimeToRot(grid, n, m):
    # Write your code here.
    q = deque()
    time = 0
    fresh = 0
    rows = len(grid)
    col = len(grid[0])
    # traversing through the matrix given
    # keeping track of no of Fresh oranges and
    # pushing the rotten ones (coordinates) on to the Stack
    for r in range(rows):
        for c in range(col):
            if grid[r][c] == 1:
                fresh+=1
            if grid[r][c] == 2:
                q.append([r, c])
    # modified BFS
    directions = [[0,1],[0,-1],[1,0],[-1,0]]
    while q and fresh>0:
        # pop an element from the queue and traverse the adjacent ones
        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                # after traversal what is the new wow and coln?
                rows_temp = dr+r
                col_temp = dc+c
                # checking this new row and coln obtained is in bound or not
                if(rows_temp<0 or rows_temp == len(grid) or
                col_temp<0 or col_temp == len(grid[0]) or
                grid[rows_temp][col_temp] != 1):
                    continue
                # else just rot the orange
                grid[rows_temp][col_temp] = 2
                q.append([rows_temp, col_temp])
                fresh-=1
        # the while operations are performed in a time interval
        time+=1
    if fresh==0:
        return time
    else:
        return -1
