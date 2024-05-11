class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the input array
        nums.sort()
        # using each no as the possible first value
        for i, a in enumerate(nums):
            # same value as before
            if i> 0 and a == nums[i-1]:
                continue
            # 2- sum (2- pointer)
            l, r = i+1, len(nums)-1
            while l<r:
                intr_sum = a + nums[l] + nums[r]
                if intr_sum > 0:
                    r -= 1
                elif intr_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # updating the pointer
                    l += 1
                    # continue updating if current left pointer value = the previous left pointer value
                    # and left pointer should not overpass the right pointer
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res


