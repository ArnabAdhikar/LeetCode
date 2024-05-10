# https://www.youtube.com/watch?v=_i4Yxeh5ceQ

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n-1):
            # Dynamic programming logic
            temp = one
            one += two
            two = temp
        return one
