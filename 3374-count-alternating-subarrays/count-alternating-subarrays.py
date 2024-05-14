class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans, curr =  0, nums[0]
        for num in nums:
            prev, curr = curr, num
            if prev^curr == 0:
                cnt = 0
            cnt+= 1
            ans+= cnt
        return ans
