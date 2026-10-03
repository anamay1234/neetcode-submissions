class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 10 1 5 6 7 1
        # 0  1 2 3 4 5

        buy = 10 

        prof = 0

        buyPrice = prices[0]

        for i in range(len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            else:
                prof = max(prices[i] - buyPrice, prof)

        
        return prof
        

