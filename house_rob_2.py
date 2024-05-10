# https://leetcode.com/problems/house-robber-ii/
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=2291s
# House rob 2

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        def rec(nums):
            r1 = 0
            r2 = 0
            for i in nums:
                temp = max(r1+i, r2)
                # shifting the values
                r1 = r2
                r2 = temp
            return max(r1, r2)
        # 1st: excluding the 0th element
        a = rec(nums[1:])
        # 2nd: just skipping the last index
        b = rec(nums[:-1])
        return max(a,b)
