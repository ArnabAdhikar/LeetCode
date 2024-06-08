class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        @cache
        def f(i, cur):
            if i >= len(nums):
                return inf
            return min(abs((cur & nums[i]) - k), abs(nums[i] - k), f(i+1, nums[i]), f(i+1, cur & nums[i]))
        return f(0, nums[0])