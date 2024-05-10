# Cheapest Flights Within K Stops
"""
Created on Wed Feb  7 20:07:51 2024

@author: ARNAB ADHIKARY
"""

class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        # declaring the price array with all infinity except the starting value
        prices = [float ("inf")]*n
        prices[src] = 0
        # continue the traversal for K+1 layers
        for i in range(k+1):
            # make a copy of the original price array after all the changes again prices = tempprices
            tempprices = prices.copy()
            # s:source, d:destination, c:cost
            for s,d,c in flights:
                # checking for the edge cases
                if prices[s] == float ("inf"):
                    continue
                # actual comparison
                if prices[s] + c < tempprices[d]:
                    tempprices[d] = prices[s]+c
            # now replace the original price with the tempprices
            prices = tempprices
        # output logic
        if prices[dst]==float ("inf"):
            return -1
        else:
            return prices[dst]
