class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # initializing the pointers
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        # contenousely checking that the pointers are not overlapping
        while left < right and top < bottom:
            # get every i in top row:
            for i in range(left, right):
                res.append(matrix[top][i])
            # just completed with the top row => update the top pointer
            top += 1
            # get every i in right col
            for i in range(top, bottom):
                # initially right pointer was placed out of bounds
                res.append(matrix[i][right-1])
            # just completed with the right most col => update the right pointer
            right -= 1
            # if pointers crossed/ overlapped
            if not(left<right and top<bottom):
                break
            # get every i in bottom row
            for i in range(right-1, left-1, -1):   # (left-1) => to include the extreme left position
                res.append(matrix[bottom-1][i])
            # done with bottomrow => update bottom pointer
            bottom -= 1
            # get every i in left most col
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
