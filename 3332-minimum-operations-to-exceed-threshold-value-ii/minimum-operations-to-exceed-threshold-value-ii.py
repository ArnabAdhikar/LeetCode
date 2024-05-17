from heapq import heapify, heappush, heappop
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Stop only when both elems are >=k
        heapify(nums)
        operations = 0
        while nums:
            minElem1 = heappop(nums)
            if nums:
                minElem2 = heappop(nums)
            else:
                return operations
            if (minElem1 < k) or (minElem2 < k):
                newElem = (min(minElem1, minElem2)*2) + max(minElem1, minElem2)
                heappush(nums, newElem)
                operations += 1
        return operations