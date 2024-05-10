# https://www.youtube.com/watch?v=5Km3utixwZs
# https://leetcode.com/problems/number-of-1-bits/description/
"""
Created on Fri Feb 23 20:14:00 2024

@author: arnab
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            # ones place
            total += n%2
            # shifting the left over bits
            n = n>>1
        return total
