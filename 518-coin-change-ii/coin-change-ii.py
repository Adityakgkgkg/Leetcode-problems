class Solution(object):
    def fun(self,sum,n , coins,memo):
        if sum == 0:
            return 1
        if sum <0 or n == 0:
            return 0
        if memo[sum][n] != -1:
            return memo[sum][n]
        take = self.fun(sum-coins[n-1],n,coins,memo)
        skip = self.fun(sum,n-1,coins,memo)
        memo[sum][n] = take+skip
        return memo[sum][n]
    def change(self, sum, coins):
        n = len(coins)
        memo = [[-1] * (n+1) for _ in range(sum +1)]
        ans = self.fun(sum,n, coins,memo)
        return ans
        