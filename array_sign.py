# Rearrange Array Element by Sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # initializing the arrays
        p, n, ans = [],[],[]
        # iterating through the nums array-> +ve and -ve integers
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        # initializing the 2 pointers
        i, j = 0, 0
        # consider j not i as i is incremented first
        while j<len(nums)//2:
            ans.append(p[i])
            i+=1
            ans.append(n[j])
            j+=1
        return ans
