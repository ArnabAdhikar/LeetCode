# Combination sum
# https://www.youtube.com/watch?v=GBKI9VSKdGg
# https://leetcode.com/problems/combination-sum/description/

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # initializing the DS
        res = []
        cur = []
        def dfs(i, cur, total):
            # base case
            if total==target:
                # we dont want to modify the cur
                res.append(cur.copy())
                return
            # cannot find any combination
            if i>=len(candidates) or total>target:
                return
            # include that candidates
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            # cleanup the cur
            cur.pop()
            # dont include
            dfs(i+1, cur, total)
        dfs(0,[],0)
        return res
