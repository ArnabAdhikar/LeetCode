# Word brak
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=5804s
# https://leetcode.com/problems/word-break/submissions/1178243784/

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # cache
        dp = [False] * (len(s)+1) # 1 extra space taken for the base case
        # base case
        dp[len(s)] = True
        # from the last index to the beginning
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                # there are enough cahracter to comapre to
                if (i+len(word))<=len(s):
                    if s[i:i+len(word)]==word:
                        # write the relation for dp
                        dp[i] = dp[i+len(word)]
                # if single way for word break is obtained then break out of the loop
                if dp[i] == True:
                    break
        return dp[0]
