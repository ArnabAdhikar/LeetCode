# https://www.youtube.com/watch?v=qMPX1AOa83k
# https://leetcode.com/problems/single-number/

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            # performing the xor operation with all the numbers
            res = i^res
        return res
