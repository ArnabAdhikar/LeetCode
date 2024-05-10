# spiral matrix

def spiralMatrix(matrix):
    # Write your code here.
    row = len(matrix)
    coln = len(matrix[0])
    left = 0
    right = coln-1
    top = 0
    bottom = row-1
    finals = []
    while top<=bottom and left<=right:
        # right
        for i in range(left, right+1):
            finals.append(matrix[top][i])
        top+=1
        # bottom
        for i in range(top, bottom+1):
            finals.append(matrix[i][right])
        right-=1
        if top<=bottom:
            # left
            for i in range(right, left-1, -1):
                finals.append(matrix[bottom][i])
            bottom-=1
        if left<=right:
            # top
            for i in range(bottom, top-1, -1):
                finals.append(matrix[i][left])
            left+=1
    return finals
