class Solution:
    # Memo - striver DP 3
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n

        def f(ind):
            if ind == 0 or ind == 1:
                return cost[ind]

            if dp[ind] != -1:
                return dp[ind]

            left = f(ind - 1) + cost[ind]

            right = float('inf')
            if ind > 1:
                right = f(ind - 2) + cost[ind]

            dp[ind] = min(left, right)
            return dp[ind]

        return min(f(n - 1), f(n - 2))