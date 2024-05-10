# https://leetcode.com/problems/decode-ways/
# https://www.youtube.com/watch?v=H9bfqozjoqs

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        # no of coins req. for 0 amount
        dp[0] = 0
        # applying dp in reverse order
        for a in range(1, amount+1):   # range(starting amt., ending amt.+1)
            # going through every coins
            for c in coins:
                # coins of amt. still req to make up the amt.=a
                cur_amt = a-c
                # if -ve current amt=out of bound
                if cur_amt>=0:
                    dp[a] = min(dp[a], dp[cur_amt]+1)
        # returning the result
        if dp[amount]!=float('inf'):
            return dp[amount]
        else:
            return -1
