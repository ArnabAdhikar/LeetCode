class Solution:
    def waysToReachStair(self, target: int) -> int:
        current_sum = 1
        ways = 0
        
        if target == 0 or target == 1:
            ways += 1
        
        pas = [[0] * 50 for _ in range(50)]
        pas[0][0] = 1
        
        for row in range(1, 50):
            pas[row][0] = 1
            for col in range(1, row + 1):
                pas[row][col] = pas[row - 1][col] + pas[row - 1][col - 1]

        for i in range(30):
            current_sum += 1 << i
            if current_sum >= target and current_sum - target <= i + 2:
                n = i + 2
                r = current_sum - target
                ways += pas[n][r]

        return ways