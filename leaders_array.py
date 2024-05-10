# Superior Elements
# https://www.youtube.com/watch?v=cHrH9CQ8pmY
# https://www.codingninjas.com/studio/problems/superior-elements_6783446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

from typing import List

def superiorElements(a : List[int]) -> List[int]:
    # declaring the variable to store the maximum nos
    maxi = 0
    ans = []
    length = len(a)
    # backside iteration of the array
    for i in range(length-1, -1, -1):
        if (a[i]>maxi):
            ans.append(a[i])
        # storing the new maximum element
        maxi = max(maxi, a[i])
    ans.sort()
    return ans
