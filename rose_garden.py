# minimum no of days to make m bouques

from typing import List

# checking whether the day is possible to consider
def possible(arr, mid, m, k):
    # k= no of flowers required
    # m= no of bouque
    counter = 0
    bouques = 0
    for i in range(len(arr)):
        if arr[i]<=mid:
            counter+=1
        # the day cannot be considered
        else:
            bouques+=(counter//k)
            counter=0
    # for 12th day
    bouques+=(counter//k)
    return bouques>=m
def roseGarden(arr: List[int], k: int, m: int):
    # m: no of bouque
    # k: no of adjacent flowers
    low = min(arr)
    high = max(arr)
    finals = high
    if (m*k)>len(arr):
        return -1
    else:
        while low<=high:
            mid = (low+high)//2
            # we got the answer at the mid
            if possible(arr, mid, m, k):
                finals = mid
                # now we need the minimum: eleminate the right half
                high = mid-1
            # if the no id too small: increase
            else:
                low = mid+1
        return finals
