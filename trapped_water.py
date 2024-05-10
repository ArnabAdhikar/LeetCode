from typing import List

def getTrappedWater(arr: List[int], n: int) -> int:
    # Write your code here.
    waterTrapped = 0
    for i in range(n):
        # finding the left max
        j = i
        leftMax = 0
        rightMax = 0
        while j >= 0:
            leftMax = max(leftMax, arr[j])
            j -= 1
        # finding the right max
        j = i
        while j < n:
            rightMax = max(rightMax, arr[j])
            j += 1
        # applying formulae
        waterTrapped += min(leftMax, rightMax) - arr[i]
    return waterTrapped
