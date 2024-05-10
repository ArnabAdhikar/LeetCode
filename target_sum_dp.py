# https://www.youtube.com/watch?v=qMky6D6YtXU&t=1796s
# https://leetcode.com/problems/target-sum/description/
"""
Created on Wed Feb 21 20:15:11 2024

@author: arnab
"""
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # initializing the hash map
        dp = {} # (index, total)-> no of ways
        def traversal(i, total):
            # reached end of the array
            if i==len(nums):
                if total==target:
                    return 1
                else:
                    return 0
            # if we have already traversef this pair
            if (i, total) in dp:
                return dp[(i, total)]
            # recursive part->
            # 2 choices-> + or -
            dp[(i, total)] = (traversal(i+1, total+nums[i])+ # +
                            traversal(i+1, total-nums[i])) # -, returns in how any cases we get the total=target
            return dp[(i, total)]
        return traversal(0, 0)
