# Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # checking the length of each of the string
        if len(s)!=len(t):
            return False
        # forming the hash map
        count_s, count_t = {}, {}
        for i in range(len(s)):
            # counting the occurances of each of the character
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        # comparing the counts of each character
        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False
        return True
