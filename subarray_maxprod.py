# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=5804s
# https://leetcode.com/problems/maximum-product-subarray/

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initializing the values
        res = max(nums)
        curmin, curmax = 1, 1
        # iterating through every single numbers
        for n in nums:
            # handelling the edge case
            if n==0:
                curmin = 1
                curmax = 1
                continue
            # keeping track of current max. and current min.
            temp = n*curmax
            curmax = max(n*curmax, n*curmin, n)  # cur. max. is modified here
            curmin = min(temp, n*curmin, n)  # we need cur. max. before it is modified
            res = max(res, curmax)
        return res
