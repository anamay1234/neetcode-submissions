class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(coins, amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            min_coins = float('inf')

            for coin in coins:
                newAmount = amount - coin
                coinsNeededTomakeNewAmount = dfs(coins, newAmount)

                if coinsNeededTomakeNewAmount >= 0:
                    min_coins = min(min_coins, coinsNeededTomakeNewAmount + 1)

            if min_coins == float('inf'):
                memo[amount] = -1
                return -1
            else:
                memo[amount] = min_coins
                return min_coins
        return dfs(coins, amount)



        