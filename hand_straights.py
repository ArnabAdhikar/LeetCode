# Hand of Straights
# https://leetcode.com/problems/hand-of-straights/description/
# https://www.youtube.com/watch?v=amnrMCVd2YI
from typing import List
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # checking the length of the array
        if len(hand) % groupSize:
            return False
        # keeping track of the no of that particular values
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        # declaring the min heap
        minheap = list(count.keys())
        # heapify
        heapq.heapify(minheap)
        # continue untill our min heap is not empty
        while minheap:
            first = minheap[0]
            # searching for the group
            for i in range(first, first+groupSize):
                # value is not available
                if i not in count:
                    return False
                # value is available
                count[i] -= 1
                # if this count = 0
                if count[i] == 0:
                    # the element that we are popping is not the minimum element
                    if i!=minheap[0]:
                        return False
                    # now we are able to pop
                    heapq.heappop(minheap)
        return True
