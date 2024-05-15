class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        # window
        l=r=0
        while r < len(nums)-1:
            farthest = 0
            # finding out the farthest index where we can jump from the current window
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            # update the window
            l = r+1
            r = farthest
            # how many jumps
            res += 1
        return res
