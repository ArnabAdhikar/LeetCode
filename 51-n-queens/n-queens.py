class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        # +ve diagonal = (r + c)
        posdiag = set()
        # -ve diagonal = (r - c)
        negdiag = set()
        res = []
        board = [["."]*n for i in range(n)]
        # backtracking row by row
        def backtrack(r):
            # base case
            if r == n:
                # making the copy of the board where each row, joined together
                copy = ["".join(row) for row in board]
                # adding the last result to the board and modifying the formatting
                res.append(copy)
                return
            # try every position in the current row
            for c in range(n):
                # checking column is already in use from the set
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                # otherwise modify the set
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                # update the board
                board[r][c] = "Q"
                # backtracking call for the next row
                backtrack(r+1)
                # cleanup for the next check
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res
