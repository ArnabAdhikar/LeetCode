class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # dimention of the matrix
        rows, cols = len(matrix), len(matrix[0])
        # BS-> 1st layer(Row)
        top, bot = 0, rows-1
        while top<=bot:
            # calculate the middle row
            row = (top+bot)//2
            # target > largest(2D Array)
            if target > matrix[row][-1]:  # looking for the right most element
                # shift the top pointer
                top = row + 1
            # target value is smaller
            elif target < matrix[row][0]: # left most element
                bot = row - 1
            # target value within this row
            else:
                break
        # none of the condition runs successfully
        if not (top <= bot):
            return False
        # BS-> 2nd layer
        row = (top+bot)//2  # fetching the current portion
        l, r = 0, cols-1
        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:   # search Right
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False
        