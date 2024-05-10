# Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1199857708/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # declaring the hash map
        count = {}
        res = 0
        l = 0
        r = 0
        for r in range(len(s)):
            # incrementing the counter
            count[s[r]] = 1 + count.get(s[r], 0)
            # redusing the window size when the no of replacements > k
            while (r-l+1)-max(count.values())>k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
