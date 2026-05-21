class Solution:
    # Memo - striver DP 3
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n

        def f(ind):
            if ind < 0:
                return 0
            if ind == 1:
                return cost[ind]

            if dp[ind] != -1:
                return dp[ind]

            dp[ind] = cost[ind] + min(f(ind - 1), f(ind - 2))
            return dp[ind]

        return min(f(n - 1), f(n - 2))