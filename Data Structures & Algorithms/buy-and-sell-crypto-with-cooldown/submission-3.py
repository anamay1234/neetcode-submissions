class Solution:
    # tabu
    def func(self, ind, canBuy, prices, dp):
        if ind >= len(prices):
            return 0

        if dp[ind][canBuy] != -1:
            return dp[ind][canBuy]

        # we can buy
        if canBuy == 1:
            # buy rn
            buy = -prices[ind] + self.func(ind+1, 0, prices, dp)

            # don't buy just yet
            dontBuyYet = self.func(ind+1, 1, prices, dp)

            dp[ind][canBuy] = max(buy, dontBuyYet)
            return dp[ind][canBuy]
        
        # we can't buy -> we need to sell 
        if canBuy == 0:
            # sell rn
            sell = prices[ind] + self.func(ind+2, 1, prices, dp)

            # don't sell just yet
            dontSellYet = self.func(ind+1, 0, prices, dp)

            dp[ind][canBuy] = max(sell, dontSellYet)
            return dp[ind][canBuy]


    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for i in range(len(prices))]

        for ind in range(len(prices) - 1, -1, -1):
            for canBuy in range(2):
                # we can buy
                if canBuy == 1:
                    # buy rn
                    buy = -prices[ind]
                    
                    if ind+1 <= len(prices) - 1:
                        buy += dp[ind+1][0]

                    # don't buy just yet
                    dontBuyYet = 0
                    if ind+1 <= len(prices) - 1:
                        dontBuyYet += dp[ind+1][1]

                    dp[ind][canBuy] = max(buy, dontBuyYet)
                
                # we can't buy -> we need to sell 
                elif canBuy == 0:
                    # sell rn
                    sell = prices[ind]
                    
                    if ind+2 <= len(prices) - 1:
                        sell += dp[ind+2][1]

                    
                    # don't sell just yet
                    dontSellYet = 0
                    if ind+1 <= len(prices) - 1:
                        dontSellYet += dp[ind+1][0]

                    dp[ind][canBuy] = max(sell, dontSellYet)


        return dp[0][1]

# base cases - we will take care of this with if statements in loops
# states in loops 
#   - canBuy went from 1 -> 0 so we make it go from 0 -> 1 in tabu
#   - ind went from 0 -> n-1 so now it is n-1 -> 0
# copy recurence

# also we will convert if to elif for tabulation


