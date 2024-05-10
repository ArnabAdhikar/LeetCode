# https://leetcode.com/problems/longest-common-subsequence/
# https://www.youtube.com/watch?v=qMky6D6YtXU

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # initializing the 2D- Grid
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        # traversal from the back side
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                # if the 2 characters are equal
                if text1[i] == text2[j]:
                    # 1+the diagonals
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    # find the maximum of the right and down values
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # result is stores at 0,0
        return dp[0][0]
