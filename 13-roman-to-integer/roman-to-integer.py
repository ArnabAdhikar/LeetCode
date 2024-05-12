class Solution:
    def romanToInt(self, s: str) -> int:
        # hash table for mapping
        roman = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C":100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            # checking the sign of the integer
            if i + 1 < len(s) and roman[s[i]]<roman[s[i+1]]:
                # -ve sign => subtract
                res -= roman[s[i]]
            else:
                # +ve sign => addition
                res += roman[s[i]]
        return res