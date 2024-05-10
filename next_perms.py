# Next Permutation
# https://leetcode.com/problems/next-permutation/description/

from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # initializing the break point index
        ind = -1
        length = len(nums)
        # finding out the break point
        for i in range(length-2, -1, -1):
            if nums[i]<nums[i+1]:
                ind = i
                break
        # no breaking point found
        if ind<0:
            nums.reverse()
        # stem- 2
        else:
            for i in range(length-1, ind, -1):
                # swapping
                if nums[i]>nums[ind]:
                    temp = nums[i]
                    nums[i] = nums[ind]
                    nums[ind] = temp
                    break
            # just reverse the 2nd part of the array
            l = ind+1
            r = length-1
            while l < r:
                nums[l] , nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
