class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            fs = dp[i - 1] + cost[i]
            ss = dp[i - 2] + cost[i]
            dp[i] = min(fs, ss)

        return min(dp[n - 1], dp[n - 2])