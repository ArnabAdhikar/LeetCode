class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index of nums1
        last = m+n-1
        # merge in reverse order
        while m>0 and n>0:
            # find the largest value
            if nums1[m-1] > nums2[n-1]:      # indexing starts from 0
                # replacing from the last
                nums1[last] = nums1[m-1]
                # update the pointer
                m -= 1
            else:
                # = or nums2 is greater
                nums1[last] = nums2[n-1]
                n -= 1
            # update last regardless
            last -= 1
        # if there is any left over elements in nums2, fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
        