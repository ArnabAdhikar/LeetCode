class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # pointer
        k = 0
        # iterating through every single values in the list
        for i in range(len(nums)):
            # perform the swap
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
