# https://leetcode.com/problems/unique-paths/description/
# https://www.youtube.com/watch?v=qMky6D6YtXU

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initializing a dummy matrix with all the values as 0
        # 2D grid
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # from the initial node to initial node, no of ways = 1
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                # val1 = left val, val2 = top val
                val1 = 0
                val2 = 0
                # loading up the values
                if(j-1 >= 0):
                    # preventing out of range.
                    val1 = dp[i][j-1]
                if(i-1 >= 0):
                    val2 = dp[i-1][j]
                # computing the no of ways and storing it in the same matrix against the same co ordinate
                dp[i][j] = dp[i][j] + val1 + val2
        return dp[m-1][n-1]
