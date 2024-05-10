# Minimum bit flip to convert a no
# https://www.youtube.com/watch?v=OOdrmcfZXd8
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # performing the XOR operation
        res = start ^ goal
        cnt = 0
        # counting the no of 1's
        while res:
            # remember
            res &= res - 1
            cnt += 1
        return cnt
