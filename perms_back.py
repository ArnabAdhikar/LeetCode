# Permutations
# https://www.youtube.com/watch?v=s7AvT7cGdSo
# https://leetcode.com/problems/permutations/description/

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        # base case
        if (len(nums)==1):
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for j in perms:
                j.append(n)
            result.extend(perms)
            nums.append(n)
        return result
