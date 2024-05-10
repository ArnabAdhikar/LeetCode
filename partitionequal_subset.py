# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=5804s
# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if the sum is odd, Partitioning is not possible
        if sum(nums)%2!=0:
            return False
        # initializing the cache
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        # traversal in reverse order
        for i in range(len(nums)-1,-1,-1):
            tempdp = set()
            for t in dp:
                tempdp.add(t + nums[i])
                # we dont want to loose the values from the original dp set after equating
                tempdp.add(t)
            dp = tempdp
        if target in dp:
            return True
        else:
            return False
