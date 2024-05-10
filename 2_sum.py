# 2 sum problem(Returning yes/ No)

def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    left = 0
    right = n-1
    book.sort()
    while left<right:
        finals = book[left]+ book[right]
        if finals==target:
            return "YES"
        elif finals<target:
            left+=1
        else:
            right-=1
    return "NO"

# 2 sum problem(Returning the index)-> Hash map

class Solution:
    def twoSum(self, nums, target):
        dick = {}
        n = len(nums)
        for i in range (n):
            remaining = target-nums[i]
            if remaining in dick:
                return [dick[remaining], i]
            dick[nums[i]] = i
        return []
