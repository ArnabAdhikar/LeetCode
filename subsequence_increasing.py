# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=5804s
# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # initializing the list
        lis = [1]*len(nums)
        # iterating through the list from the backside
        for i in range(len(nums)-1, -1,-1):
            # iterating every sub-sequence after i
            for j in range(i+1, len(nums)):
                # we need increasing subsequence
                if nums[i]<nums[j]:
                    # updating the length of longest subsequence
                    lis[i] = max(lis[i], 1+lis[j])
        return max(lis)
