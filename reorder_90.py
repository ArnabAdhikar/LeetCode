# Rotate Image
# https://leetcode.com/problems/rotate-image/description/
# https://www.youtube.com/watch?v=fMSJSS7eO1w

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # setting the left and right boundary
        l, r = 0, len(matrix[0])-1
        while l<r:
            # iterating through the matrix
            for i in range(r - l):
                # pointer allocation
                top, bottom = l, r

                # save the top left
                topleft = matrix[top][l + i]
                # moving bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # moveing bottom right into into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move top left into top right(overriting)
                matrix[top + i][r] = topleft
            # update the pointer
            r -= 1
            l += 1
