# Count Number of Nice
# https://www.youtube.com/watch?v=oGmTyjy8rI8
# https://leetcode.com/problems/count-number-of-nice-subarrays/submissions/1213649280/

from typing import List
class Solution:
    def atmostk(self, nums, k):
        i,j,res = 0,0,0
        while j<len(nums):
            # odd no
            if nums[j]%2==1:
                if k>0:
                    # got an odd sum now the neftocer requirements also reduced
                    k-=1
                else:
                    # got an even no, shift the i-> modify the window
                    while nums[i]%2!=1:
                        i+=1
                    i+=1
            res += (j-i+1)
            j += 1
        return res
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atmostk(nums,k)-self.atmostk(nums,k-1)
