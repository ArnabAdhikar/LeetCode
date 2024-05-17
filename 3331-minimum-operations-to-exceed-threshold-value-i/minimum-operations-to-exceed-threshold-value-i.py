class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(map(k.__gt__, nums))