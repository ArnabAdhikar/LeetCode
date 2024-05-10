# Edit Distance
# https://www.youtube.com/watch?v=XYi2-LPrwm4
# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 2D array initialization
        cache = [[float("inf")]*(len(word2)+1) for i in range (len(word1)+1)]
        for j in range(len(word2)+1):
            # initializing the last row(base case)
            cache[len(word1)][j] = len(word2)-j
        for i in range(len(word1)+1):
            # initializing the last column(base case)
            cache[i][len(word2)] = len(word1)-i
        # bottom up and right to left DP
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    # computing minimum no of operations
                    cache[i][j] = cache[i+1][j+1] # just shift the characters
                else:
                    # check minimum between the Insert, Delete and Replace operations
                    # Insert=right side; Delete=bellow; Replace=diagonal
                    cache[i][j] = 1 + min(cache[i][j+1],cache[i+1][j],cache[i+1][j+1])
        return cache[0][0]
