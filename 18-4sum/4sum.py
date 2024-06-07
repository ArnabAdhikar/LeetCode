class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the array
        nums.sort()
        res, quad = [], []

        def KSum(k, start, target):
            # non base case
            if k!=2:
                # iterate through the array except the last k elements
                for i in range(start, len(nums)-k+1):
                    # eleminating the duplicates
                    # for the starting value we don't want to execute this
                    if i> start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    KSum(k-1, i+1, target-nums[i])
                    quad.pop()
                return
            # base case
            l, r = start, len(nums)-1
            while l<r:
                if nums[l]+nums[r] < target:
                    l += 1
                elif nums[l]+nums[r] > target:
                    r -= 1
                else:
                    # adding up 2 lists
                    res.append(quad + [nums[l], nums[r]])
                    # updating the pointer
                    l += 1
                    # same value is not acceptable ans should be in bounds
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        KSum(4, 0, target)
        return res
