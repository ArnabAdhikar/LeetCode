# https://leetcode.com/problems/longest-palindromic-substring/
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=2291s

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        # initially left and right pointer points at the middle of the character
        # and then expand from the middle
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        res = s[0]
        for i in range(len(s)):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)
            # now checking the length contenousely
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res
