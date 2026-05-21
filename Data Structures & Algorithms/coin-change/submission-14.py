class Solution:
    #brute force
    def func(self, coins, remainder, dp):
        if remainder == 0:
            return 0

        if dp[remainder] is not None:
            return dp[remainder]

        minCoins = float('inf')

        # take each coin
        for i in range(len(coins)):
            if remainder - coins[i] >= 0:
                coinsNeededToMakeRemainder = self.func(coins, remainder - coins[i], dp)

                if coinsNeededToMakeRemainder >= 0:
                    take = 1 + coinsNeededToMakeRemainder
                    minCoins = min(minCoins, take)
        
        if minCoins == float('inf'):
            dp[remainder] = -1
            return dp[remainder]
        else:
            dp[remainder] = minCoins
            return dp[remainder]


    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)
        return self.func(coins, amount, dp)