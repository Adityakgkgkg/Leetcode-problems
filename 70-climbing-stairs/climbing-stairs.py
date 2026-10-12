class Solution(object):
    def climbStairs(self, n):
        dp = {}
        def solve(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i in dp:
                return dp[i]
            dp[i] = solve(i-1) + solve(i-2)
            return dp[i]
        return solve(n)

        