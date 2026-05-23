class Solution:
    # memo
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
        return self.func(0, 1, prices, dp)


