# Sum of Subarray Minimus
# https://leetcode.com/problems/sum-of-subarray-minimums/
# https://www.youtube.com/watch?v=aX1F2-DrBkQ

from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9+7
        res = 0
        # (index, num)
        stack = []
        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j,m = stack.pop()
                # if the stackis non empty
                if stack:
                    left = j-stack[-1][0]
                else:
                    left = j+1
                right = i-j
                res = (res+m*left*right)%mod
            stack.append((i,n))
        for i in range(len(stack)):
            j, n = stack[i]
            left = j-stack[i-1][0] if i>0 else j+1
            right = len(arr)-j
            res = (res+n*left*right)%mod
        return res
