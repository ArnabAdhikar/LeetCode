class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # simultenousely iterate
        for i in range(len(strs[0])):
            for s in strs:
                # if the forst character doesn't matches
                # if and only if i is in bounds
                if i==len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
