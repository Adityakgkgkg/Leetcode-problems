class Solution(object):
    def fun(self,amount,n,coins,memo):
        if amount== 0:
            return 0
        if amount <0 or n==0:
            return float('inf')
        if memo[amount][n] != -1:
            return memo[amount][n]
        take =1 + self.fun(
            amount-coins[n-1], n,coins,memo
        ) 
        skip = self.fun(
            amount, n-1,coins,memo
        )
        memo[amount][n] = min(skip,take)
        return memo[amount][n]
    def coinChange(self, coins, amount):
       n = len(coins)
       memo = [[-1] * (n+1) for _ in range(amount+1)]
       ans = self.fun(amount,n,coins,memo)
       return -1 if ans==float('inf') else ans
        