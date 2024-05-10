# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
# https://www.youtube.com/watch?v=qMky6D6YtXU&t=1796s
"""
Spyder Editor

This is a temporary script file.
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # defining the hash map
        dp = {}
        # key = (index, buy/sell), value = max_profit
        def dfs(i, buying):
            # out of bounds
            if i>=len(prices):
                return 0
            # already stored max profit against this key
            if (i, buying) in dp:
                return dp[(i, buying)]
            # now checking the condition for buying/ Selling
            # buy-> i+1
            # sell-> i+2, we have to leave 1 day for cooldown
            if buying:
                # 2 choices-> Buying/ cooldown
                # we spend some money
                buy = dfs(i+1, not buying) - prices[i] # after buying we cannot buy it again
                cooldown = dfs(i+1, buying)
                # caching
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # we made some money
                sell = dfs(i+2, not buying) + prices[i] # now, we cannot buy anything
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i,buying)]
        return dfs(0, True)
