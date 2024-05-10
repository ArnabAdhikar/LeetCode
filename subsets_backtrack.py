# Subsets
# https://www.youtube.com/watch?v=REOH22Xwdkk
# https://leetcode.com/problems/subsets/

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        res = []
        subset = []
        def dfs(i):
            # checking the bounds
            if i >= len(nums):
                # append the sunsets formed till now
                res.append(subset.copy())
                return
            # include nums[i]->left
            subset.append(nums[i])
            dfs(i+1)
            # don't include nums[i]->right
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
