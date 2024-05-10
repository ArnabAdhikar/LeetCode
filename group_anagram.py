# group Anagram
# https://www.youtube.com/watch?v=vzdNOK2oB2E
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # counting the characters in a string
                count[ord(c)-ord("a")] += 1
            # mapping with the string
            res[tuple(count)].append(s)
        return res.values()
