class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = {}
        def solve(i):
            if i <= 1:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = min ( solve(i-1) + cost[i-1],
                solve(i-2) + cost[i-2]
            )
            return dp[i]
        return solve(n)
        