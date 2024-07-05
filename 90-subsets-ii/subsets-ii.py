class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # first sort the array
        nums.sort()
        def backtrack(i, subset):   # keeping track of index in nums array, current subset looking like
            # base case
            if i==len(nums):
                res.append(subset.copy())
                return

            # All subset that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            # cleanup(for this step)
            subset.pop()

            # All subset that don't include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:   # skip the duplicate values
                i += 1
            # we want [] included
            backtrack(i+1, subset)
            
        backtrack(0, [])
        return res
