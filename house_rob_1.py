# https://leetcode.com/problems/house-robber/submissions/1175213499/?source=submission-ac
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=2291s

class Solution:
    def rob(self, nums: list[int]) -> int:
        # edge case
        if len(nums) < 3:
            return max(nums)
        # initializing the previous and the current
        # always selecting the first element
        prev = nums[0]
        curr = max(nums[0], nums[1])
        # skipping the second and starting from the 3rd
        for n in range(2, len(nums)):
            # modifying the current first
            curr = max(nums[n]+prev, curr)
            # shifting the pointer
            prev = curr
        return curr
