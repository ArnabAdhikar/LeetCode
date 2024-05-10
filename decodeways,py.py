# https://leetcode.com/problems/decode-ways/
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=2291s

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        # initializing a cache
        n = len(s)
        dp = [0] * (n + 1)
        # one way to decode an empty string and a string of length 1
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])
            if one_digit != 0:
                # consider the current digit as a single character.
                dp[i] += dp[i - 1]
            if 10 <= two_digits <= 26:
                # consider the current two digits as a single character.
                dp[i] += dp[i - 2]
        return dp[n]
