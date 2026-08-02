class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProf = 0


        L = 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                prof = prices[R] - prices[L]
                maxProf = max(maxProf, prof)

        return maxProf
        