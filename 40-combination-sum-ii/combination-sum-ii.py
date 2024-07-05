class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the array
        candidates.sort()
        res = []
        def backtrack(cur, pos, target):    # pos -> starting position
            # base case
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return
            # for keeping track of the previous element just chosen
            prev = -1
            for i in range(pos, len(candidates)):
                # that perticular candidate already chosen in the previous combination
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                # (i+1) -> choose any other elements
                backtrack(cur, i+1, target - candidates[i])
                # cleanup
                cur.pop()
                # updating the previous pointer
                prev = candidates[i]
        backtrack([], 0, target)
        return res
