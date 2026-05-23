class Solution:
    # tabu
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
        dp = [[0] * (amount + 1) for i in range(len(coins))]

        for ind in range(len(coins)):
            dp[ind][0] = 1

        for amnt in range(amount+1):
            if amnt % coins[0] == 0:
                dp[0][amnt] = 1
            else:
                dp[0][amnt] = 0


        for ind in range(1, len(coins)):
            for amount in range(1, amount+1):
                    totalNumOfWays = 0

                    # pick
                    pick = 0
                    newAmount = amount - coins[ind]
                    if newAmount >= 0:
                        pick = dp[ind][newAmount]

                    dontPick = dp[ind - 1][amount]
                    
                    dp[ind][amount] = pick + dontPick


        return dp[len(coins) - 1][amount]


# Bases cases
# States in loops (backwards)
# Copy Recurence
#
#
