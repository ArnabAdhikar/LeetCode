# Number of Substrings Containing All Three Characters
# https://www.youtube.com/watch?v=VNL2VhDxj7U
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        index_a, index_b, index_c = -1, -1, -1
        for i, x in enumerate(s):
            if x=='a':
                index_a = i
            elif x=='b':
                index_b = i
            else:
                index_c = i
            if i>1:
                count += min([index_a, index_b, index_c])+1
        return count
