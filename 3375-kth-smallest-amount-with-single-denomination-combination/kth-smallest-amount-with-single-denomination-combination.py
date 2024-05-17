class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        def fn(val): 
            """Return number of denominations <= val."""
            ans = 0 
            for i in range(1, n+1): 
                for comb in combinations(coins, i): 
                    x = lcm(*comb)
                    ans -= pow(-1, i)*(val//x)
            return ans 
        lo, hi = 0, k*min(coins)
        while lo < hi: 
            mid = lo + hi >> 1
            if fn(mid) < k: lo = mid+1 
            else: hi = mid 
        return lo
