class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            else:
                num_set.add(i)
        return False
