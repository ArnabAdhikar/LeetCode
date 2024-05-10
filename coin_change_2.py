# Coin change 2
# https://www.youtube.com/watch?v=Mjy4hd2xgrs
# https://leetcode.com/problems/coin-change-ii/description/

from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp cache/ matrix initialization
        dp = [[0] * (len(coins)+1) for i in range(amount+1)]
        dp[0] = [1] * (len(coins) + 1)
        # different ways we can sum up to the ammount from 1
        for a in range(1, amount+1):
            # following the bottom up approach
            for i in range(len(coins)-1, -1, -1):
                # i-> no of available coins; a-> ammount
                dp[a][i] = dp[a][i+1]   # skip that coin, else
                # check the bounds, - ve-> out of bounds
                if a-coins[i]>=0:
                    dp[a][i] += dp[a-coins[i]][i]
        return dp[amount][0]
