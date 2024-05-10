# counting bits
# https://leetcode.com/problems/counting-bits/

from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = []
        for i in range(n+1):
            total = 0
            while i:
                # ones place
                total += i%2
                # shifting the left over bits
                i = i>>1
            counter.append(total)
        return counter
