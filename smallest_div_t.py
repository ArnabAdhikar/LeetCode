# Find the Smallest Divisor Given a Threshold
# https://www.youtube.com/watch?v=UvBKTVaG6U8
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

from typing import List
from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # initializing the bound
        l = 1
        r = max(nums)
        while l <= r:
            mid = (l + r) // 2
            if sum(ceil(j / mid) for j in nums) <= threshold:
                r = mid - 1
            else:
                l = mid + 1
        return l
