class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        # hash map
        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1
        # DFS backtracking function
        def dfs():
            # base case
            # no more values left to choose for that permutation
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in count:
                # enough values left
                if count[n] > 0:
                    # add to the current permutation
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    # cleanup
                    count[n] += 1
                    perm.pop()
        dfs()
        return res
