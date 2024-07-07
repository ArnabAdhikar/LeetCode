class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        while numBottles > 0:
            # first drink these bottles
            res += numBottles
            # keep track of empty bottles
            empty += numBottles
            # calculate no of full bottles
            numBottles = empty//numExchange
            # any bottles that we cannot exchange
            empty = empty%numExchange
        return res
