# Longest Palindromic Subsequence
# https://www.youtube.com/watch?v=bUr8cNWI09Q&t=891s
# https://leetcode.com/problems/longest-palindromic-subsequence/submissions/1249207171/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        def dfs(i, j):
            # out of bounds case
            if i<0 or j==len(s):
                return 0
            # if i ad j already processed
            if (i,j) in cache:
                return cache[(i, j)]
            # if the characters at both of the position matches
            if s[i] == s[j]:
                # calculating the length of the subsequences
                # i and j on same character
                if i==j:
                    length = 1
                # i and j on the different caharacters
                else:
                    length = 2
                cache[(i, j)] = length + dfs(i-1, j+1)
            # if the cahracters are different
            else:
                # branch in both the directions
                cache[(i, j)] = max(dfs(i-1, j), dfs(i, j+1)) # left shift, right shift
            return cache[(i, j)]
        for i in range(len(s)):
            # for getting even sub sequences
            dfs(i, i)
            # for getting odd sub sequences
            dfs(i, i+1)
        # finding the longest value
        return max(cache.values())
