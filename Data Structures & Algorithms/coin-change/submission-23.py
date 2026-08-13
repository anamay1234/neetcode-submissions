class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        dp[0] = 0

        for target in range(1, amount + 1):
            minAmtOfCoins = float("inf")
            
            for coin in coins:
                if target - coin >= 0:
                    call = dp[target - coin]
                    if call != float("inf"):
                        call += 1
                        minAmtOfCoins = min(minAmtOfCoins, call)

            dp[target] = minAmtOfCoins

        res = dp[amount]

        if res == float("inf"):
            return -1
        else:
            return res


        def dfs(target):
            if target == 0:
                return 0

            if dp[target] != -1:
                return dp[target]

            minAmtOfCoins = float("inf")
            
            for coin in coins:
                if target - coin >= 0:
                    call = dfs(target - coin)
                    if call != float("inf"):
                        call += 1
                        minAmtOfCoins = min(minAmtOfCoins, call)

            dp[target] = minAmtOfCoins
            return dp[target]

        
        funcCall = dfs(amount)

        if funcCall == float("inf"):
            return -1
        else:
            return funcCall