# Assign Cookies
# https://leetcode.com/problems/assign-cookies/
# https://www.youtube.com/watch?v=JW8fgvoxPTg
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sorting both of the array
        g.sort()
        s.sort()
        # 2 pointers, i-> no of kids we made happy
        i = j = 0
        # if i is inbound
        while i<len(g):
            # greed factor greater than the size of the cookie=> shift the j pointer
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j == len(s):
                break
            i += 1
            j += 1   # we are using up the cookie
        return i
