class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left and the right pointer
        l, r = 0, len(nums) - 1
        i = 0
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        # iterate the entire array untill i crosses the Right pointer
        while i<=r:
            if nums[i] == 0:
                # swap between left and i
                swap(l, i)
                l+=1
            elif nums[i] == 2:
                # swap between i and Right and don't increment i
                swap(i, r)
                r -= 1
                # nutrilize the incrementation in i
                i -= 1
            # increment i in other cases
            i += 1
