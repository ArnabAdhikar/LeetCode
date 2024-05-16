class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[[-1, 1e9] for i in range(1<<(n-1))] for j in range((n - 1))]
        for i in range(n-1): # take i + 1
            dp[i][1<<i] = [-1, abs(i+1-nums[0])]
        for k in range(1 << (n-1)):
            for j in range(n-1):
                if k & (1<<j):
                    for i in range(n-1):
                        if i == j:
                            continue
                        if k & (1<<i):
                            if dp[i][k ^ (1<<j)][1] + abs(j + 1 - nums[i+1]) < dp[j][k][1]:
                                dp[j][k] = [i, dp[i][k ^ (1<<j)][1] + abs(j+1 - nums[i+1])]
        st = -1
        stsc = 1e9
        for i in range(n-1):
            if dp[i][-1][1] + abs(-nums[i+1]) < stsc:
                st = i
                stsc = dp[i][(1<<(n-1)) - 1][1] + abs(-nums[i+1])
        ans = [0]
        pre = st
        nowmask = (1<<(n-1)) - 1
        while pre != -1:
            ans.append(pre+1)
            p = pre
            pre = dp[pre][nowmask][0]
            nowmask ^= 1<<p
        return ans