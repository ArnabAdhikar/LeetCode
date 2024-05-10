# https://leetcode.com/problems/palindromic-substrings/description/
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=2291s

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        counter = 0
        if len(s) <= 1:
            return 1
        # initially left and right pointer points at the middle of the character
        # and then expand from the middle
        def expand_from_center(left, right):
            c = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                c+=1
            return c
        for i in range(len(s)):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)
            # contenousely adding up the values
            counter+=odd+even
        return counter
