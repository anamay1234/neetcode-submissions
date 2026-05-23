class Solution:
    # memo
    def func(self, ind, amount, coins, dp): 
        if amount == 0:
            return 1

        if ind == 0:
            if amount % coins[0] == 0:
                return 1
            else:
                return 0

        if dp[ind][amount] != -1:
            return dp[ind][amount]

        totalNumOfWays = 0

        # pick
        pick = 0

        newAmount = amount - coins[ind]
        if newAmount >= 0:
            pick = self.func(ind, newAmount, coins, dp)

        dontPick = self.func(ind - 1, amount, coins, dp)
        
        dp[ind][amount] = pick + dontPick
        return dp[ind][amount]
            
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for i in range(len(coins))]
        return self.func(len(coins) - 1, amount, coins, dp)