class Solution(object):
    def solve(self,coins,n,amount,memo):
        if amount == 0:
            return 1
        if amount < 0 or n==0:
            return 0
        if memo[amount][n] != -1:
            return memo[amount][n]
        take = self.solve(coins,n,amount-coins[n-1],memo)
        skip = self.solve(coins,n-1,amount,memo)
        memo[amount][n] = take + skip
        return memo[amount][n]

    def change(self,amount,coins):
        n=len(coins)
        memo = [[-1] * (n+1) for _ in range(amount +1)]
        return self.solve(coins,n,amount,memo)
        