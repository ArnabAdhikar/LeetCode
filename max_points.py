# Maximum Points You Can Obtain from Cards
# https://www.youtube.com/watch?v=TsA4vbtfCvo
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # initializing the points
        l, r = 0, len(cardPoints)-k
        # get the sum of last k elements
        total = sum(cardPoints[r:])
        # initial result
        res = total
        # sliding the window untill the right is inbound
        while r<len(cardPoints):
            # main computation
            total += (cardPoints[l] - cardPoints[r])
            res = max(res, total)
            # then perform the slide operations
            l += 1
            r += 1
        return res
