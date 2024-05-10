# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# https://www.youtube.com/watch?v=XEmy13g1Qxc&t=1s

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # target index
        k = len(nums)-k
        # Quick Select algorithm
        def quickselect(l, r):
            pivot, p = nums[r], l
            # iterate throug the entire array except the last element
            for i in range(l,r):
                if nums[i]<=pivot:
                    # swap
                    nums[p], nums[i]=nums[i], nums[p]
                    # after every swap increment the p pointer
                    p+=1
            # last-> swap the values betwween the right most element and pth value
            nums[p], nums[r] = nums[r], nums[p]
            # run the quick select in left portion
            if p>k:
                return quickselect(l, p-1)
            # right portion
            elif p<k:
                return quickselect(p+1, r)
            # got the answer
            else:
                return nums[p]
        return quickselect(0, len(nums)-1)
