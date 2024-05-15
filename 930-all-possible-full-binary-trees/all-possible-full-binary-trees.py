# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # caching
        dp = {}
        def backtrack(n):
            # base case
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            # n is already computed
            if n in dp:
                return dp[n]
            res = []
            # brutforcing (0 - n-1)
            for l in range(n):
                # main op
                r = n-1-l
                lefttree = backtrack(l)
                righttree = backtrack(r)
                # create the full binary tree
                for t1 in lefttree:
                    for t2 in righttree:
                        # rootnode = 0
                        res.append(TreeNode(0, t1, t2))
            # cache the result before returning
            dp[n] = res
            return res
        return backtrack(n)
