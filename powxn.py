# Pow(x, n)
# https://www.youtube.com/watch?v=g9YQyYi4IQQ&t=2s
# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # devide and conquore-> recursion
        def helper(x, n):
            # base case
            if x==0:
                return 0
            if n == 0:
                return 1
            res = helper(x, n//2)
            res = res*res
            # handelling the odd exponents
            if n%2!=0:
                return x*res
            else:
                return res
        res = helper(x, abs(n))
        if n >= 0:
            return res
        else:
            # handelling the -ve power
            return 1/res
