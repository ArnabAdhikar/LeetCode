# Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
# https://www.youtube.com/watch?v=j4JDr4-jvo4&t=1s

from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # count no of subarrays with current goal<=x
        def helper(x):
            # if the goal is -ve
            if x<0:
                return 0
            # l-> Left Pointer
            # r-> Right Pointer
            res, l, cur = 0, 0, 0
            for r in range(len(nums)):
                # keeping track of current total
                cur += nums[r]
                while cur > x:
                    # shift the window and modify the current sum
                    cur -= nums[l]
                    l += 1
                res += (r-l+1)
            return res
        return helper(goal)-helper(goal-1)
