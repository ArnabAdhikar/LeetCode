class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        # hash map
        hashmap = {"2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "qprs",
                    "8" : "tuv",
                    "9" : "wxyz"}
        # backtracking
        def backtrack(i, curstr):
            # base case
            # we have finished building current string
            if len(curstr) == len(digits):
                res.append(curstr)
                return
            # building the current string
            for c in hashmap[digits[i]]:   # string against the digit
                backtrack(i + 1, curstr + c)
        # call backtrack if digit string is non empty
        if digits:
            backtrack(0, "")
        return res
        