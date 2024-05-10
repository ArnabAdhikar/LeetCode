# set matrix 0

def zeroMatrix(matrix, n, m):
    # Write your code here.
    row = [0]*n
    coln = [0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                coln[j]=1
    for i in range(n):
        for j in range(m):
            if row[i] or coln[j] == 1:
                matrix[i][j]=0
    return matrix
