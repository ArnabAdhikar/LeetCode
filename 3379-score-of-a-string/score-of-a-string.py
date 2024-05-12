class Solution:
    def scoreOfString(self, s: str) -> int:
        absdiff = lambda x: abs(ord(x[0]) - ord(x[1]))
        return sum(map(absdiff,pairwise(s)))
