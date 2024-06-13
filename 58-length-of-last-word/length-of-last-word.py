class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # initializing the pointers
        i, length = len(s)-1, 0
        # eleminating the leading white spaces
        while s[i]==" ":
            i -= 1
        # determining the leangth
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
