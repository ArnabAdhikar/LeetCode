class Solution:
    def convert(self, s: str, numrows: int) -> str:
        if numrows == 1:
            return s
        res = ""
        # traversing through the rows
        for r in range(numrows):
            increment = 2*(numrows-1)
            # works perfectly for first row and last row
            for i in range(r, len(s), increment):
                res += s[i]
                # rows in between has extra values
                # (i+increment-2*r) index of this value and should not go out of bounds
                if (r>0 and r<numrows-1 and i+increment-2*r < len(s)):
                    res += s[i+increment-2*r]
        return res
