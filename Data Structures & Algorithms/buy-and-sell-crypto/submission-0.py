class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumPriceToBuy = prices[0]
        runningMaxProfit = 0
        for i in range(len(prices)):
            netProfit = prices[i] - minimumPriceToBuy
            runningMaxProfit = max(runningMaxProfit, netProfit)
            minimumPriceToBuy = min(minimumPriceToBuy, prices[i])

        return runningMaxProfit

