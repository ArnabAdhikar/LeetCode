# buy sell

def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    min_limit = 10**9
    profit = 0
    for i in prices:
        min_limit = min(min_limit, i)
        profit = max(profit, i-min_limit)
    return profit
