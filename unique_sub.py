# Unique Substring
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1199757699/
# https://www.youtube.com/watch?v=wiGpQwVHdE0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        r = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res = max(res, r-l+1)
        return res
