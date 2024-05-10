# 0/1 matrix

def nearest(mat,n,m):
    # n-> Rows; m-> Columns
    dist = [[9999999 for i in range(m)] for j in range(n)]
    # for each cell
    for i in range(n):
        for j in range(m):
            # traverse the whole matrix
            for k in range(n):
                for l in range(m):
                    # if the cell contains 1 
                    if (mat[k][l] == 1):
                        dist[i][j] = min(dist[i][j], abs(i - k) + abs(j - l))
    return dist
##################### BFS ####################################################  
def nearest2(mat, n, m):
    q = []
    dist = [[9999999 for i in range(m)] for j in range(n)]
    # Push the coordinates of cells containing 1 in the queue.
    for i in range(n):
        for j in range(m):
            if (mat[i][j] == 1):
                q.append([i, j])
                dist[i][j] = 0
    # To move up, down, left, right.
    x_dir = [-1, 0, 1, 0]
    y_dir = [0, -1, 0, 1]
    # BFS performed.
    while (len(q)):
        temp = q.pop()
        row = temp[0]
        col = temp[1]
        # All adjacent cells checked.
        for k in range(4):
            x_new = row + x_dir[k]
            y_new = col + y_dir[k]
            ''' 
            	Conditions to check if adjacent cell lie in 
                matrix and to minimum distance is updated.
            '''
            if (x_new >= 0 and x_new < n and y_new >= 0 and y_new < m and dist[x_new][y_new] > dist[row][col] + 1):
                dist[x_new][y_new] = dist[row][col] + 1
                q.append([x_new, y_new])
    return dist
