# interleaving Strings
# https://www.youtube.com/watch?v=3Rw3p9LrgvE
# https://leetcode.com/problems/interleaving-string/description/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Checking for the validity of the string
        if len(s1)+len(s2) != len(s3):
            return False
        # initializing the 2D grid with all the values as False
        dp = [[False]*(len(s2)+1) for i in range(len(s1)+1)]
        # the corner value will always be True
        dp[len(s1)][len(s2)] = True
        # Traversing the grid from the bottom right to the top left
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # i in bounds-> is that character = the target character
                # and dp[i+1][j] = True
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j] == True:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1] == True:
                    dp[i][j] = True
        return dp[0][0]
