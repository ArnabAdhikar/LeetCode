class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Hash Set -> Unique character
        charset = set()
        # check for duplicate characters
        def overlap(charset, s):
            # temporary set
            prev = set()
            for c in s:
                if c in charset or c in prev:
                    return True
                prev.add(c)
            return False
        def backtrack(i):
            # already gone through the entire array
            if i == len(arr):
                return len(charset)
            res = 0
            # not overlapping character -> add
            if not overlap(charset, arr[i]):
                for c in arr[i]:
                    charset.add(c)
                # continue the same result from index i+1
                res = backtrack(i+1)
                # cleanup from the backtracking
                for c in arr[i]:
                    charset.remove(c)
            return max(res, backtrack(i+1))
        return backtrack(0)
